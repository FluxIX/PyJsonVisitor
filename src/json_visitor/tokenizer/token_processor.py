from typing import Any, Dict, Callable, TextIO, Union
import ijson
from io import StringIO
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
        }

    @property
    def _scope_walker( self ) -> ScopeWalker:
        """
        Gets the scope walker the tokenizer uses to walk the JSON tree.

        Returns:
            Scope walker the tokenizer uses to walk the JSON tree.
        """

        return self._internal_scope_walker

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

        self._internal_scope_walker.process_document_start()

        for event, value in ijson.basic_parse( source_file ):
            handler = self._event_handlers.get( event, None )
            if handler is not None:
                handler( value )

        self._internal_scope_walker.process_document_end()
