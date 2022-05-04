__version__ = r"1.1.1"

from typing import Any, Dict, List, Tuple, Callable, TextIO, Union

import ijson
from collections.abc import Iterable
from enum import Enum, auto
from io import StringIO
from ..scoping.scope_types import ScopeTypes
from .scope_walker import ScopeWalker

class TokenProcessor( object ):
    """
    Implements a JSON tokenizer and uses the tokens to publish events through the Visitor interface.
    """

    def __init__( self, scope_walker: ScopeWalker ):
        self._internal_scope_walker: ScopeWalker = scope_walker

        self._event_handlers: Dict[ str, Callable[ [ Any ], None ] ] = {
            "start_map": self._scope_walker.process_start_map,
            "map_key": self._scope_walker.process_map_key,
            "end_map": self._scope_walker.process_end_map,
            "start_array": self._scope_walker.process_start_array,
            "end_array": self._scope_walker.process_end_array,
            "number": self._scope_walker.process_value,
            "string": self._scope_walker.process_value,
            "boolean": self._scope_walker.process_value,
            "null": self._scope_walker.process_value,
            "value": self._scope_walker.process_value,
        }

    @property
    def _scope_walker( self ) -> ScopeWalker:
        """
        Gets the scope walker the tokenizer uses to walk the JSON tree.

        Returns:
            Scope walker the tokenizer uses to walk the JSON tree.
        """

        return self._internal_scope_walker

    def _process_events( self, event_source: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Processes events from the given event source and walks through the scopes associated with the events.

        Parameters:
            `event_source`: Iterable of the events.

        Returns:
            None
        """

        self._internal_scope_walker.process_document_start()

        for event, value in event_source:
            handler = self._event_handlers.get( event, None )
            if handler is not None:
                handler( value )

        self._internal_scope_walker.process_document_end()

    def process( self, input_source: Union[ TextIO, str ] ) -> None:
        """
        Tokenizes the input and processes the tokens, pushing the walk sequence through the adapters in the scope walker.

        Parameters:
            `input_source`: text file-object or string containing the input to process.

        Returns:
            None
        """

        if input_source is None:
            raise ValueError( "Input source cannot be None." )
        elif isinstance( input_source, str ):
            source_file = StringIO( input_source )
        else:
            source_file = input_source

        self._process_events( ijson.basic_parse( source_file ) )

    def _generate_events_from_json( self, input_json: Any ):
        class NodeTypes( Enum ):
            Event = auto()
            Item = auto()

        def get_scope_type( item: Any ) -> ScopeTypes:
            if isinstance( item, list ):
                result = ScopeTypes.List
            elif isinstance( item, dict ):
                result = ScopeTypes.Object
            else:
                result = ScopeTypes.Value

            return result

        items_to_process: List[ Tuple[ NodeTypes, Union[ List[ Tuple[ ScopeTypes, List[ Any ] ] ], Tuple[ str, Any ] ] ] ] = [ ( NodeTypes.Item, ( None, input_json ) ) ]
        while len( items_to_process ) > 0:
            items_processing: Tuple[ NodeTypes, Union[ List[ Tuple[ ScopeTypes, List[ Any ] ] ], Tuple[ str, Any ] ] ] = items_to_process.pop()
            node_type, value = items_processing

            if node_type == NodeTypes.Event:
                yield value
            elif node_type == NodeTypes.Item:
                scope_type, items = value
                if scope_type == ScopeTypes.Object:
                    item = items[ 0 ]

                    new_items = [ ( NodeTypes.Event, ( "start_map", None ) ),
                                  ( NodeTypes.Item, ( ScopeTypes.Member, [ ( key, item[ key] ) for key in item ] ) ),
                                  ( NodeTypes.Event, ( "end_map", None ) ),
                                ]
                elif scope_type == ScopeTypes.Member:
                    new_items = []
                    for item in items:
                        key, value = item

                        new_items.append( ( NodeTypes.Event, ( "map_key", key ) ) )
                        new_items.append( ( NodeTypes.Item, ( get_scope_type( value ), value ) ) )
                elif scope_type == ScopeTypes.List:
                    new_items = []
                    for item in items:
                        new_items.append( ( NodeTypes.Event, ( "start_array", None ) ) )
                        new_items.append( ( NodeTypes.Item, ( get_scope_type( item ), item ) ) )
                        new_items.append( ( NodeTypes.Event, ( "end_array", None ) ) )
                elif scope_type == ScopeTypes.Value:
                    new_items = [ ( NodeTypes.Event, ( "value", items ) ) ]
                else: # if scope_type == None: # The scope type is unknown; detect the type and reprocess.
                    new_items = [ ( NodeTypes.Item, ( get_scope_type( items ), items ) ) ]

                items_to_process.extend( reversed( new_items ) )

    def process_json( self, input_source: Any ) -> None:
        """
        Tokenizes the input and processes the tokens, pushing the walk sequence through the adapters in the scope walker.

        Parameters:
            `input_source`: a valid Python-representation of a valid JSON value.

        Returns:
            None
        """

        self._process_events( self._generate_events_from_json( input_source ) )
