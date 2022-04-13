from typing import Union, TextIO

from .simple_adapters.base_adapter import BaseAdapter as SimpleBaseAdapter
from .tokenizer.scope_walker import ScopeWalker
from .tokenizer.token_processor import TokenProcessor

class JsonVisitor( object ):
    """
    Implements a visitor for JSON nodes in a JSON object using the Visitor pattern.
    
    Notes:
        - Visitor pattern: https://en.wikipedia.org/wiki/Visitor_pattern
    """

    def __init__( self, adapter: SimpleBaseAdapter ):
        if not isinstance( adapter, SimpleBaseAdapter ):
            raise ValueError( f"Adapter must be an instance of { SimpleBaseAdapter.__qualname__ }." )
        else:
            self._target_adapter: SimpleBaseAdapter = adapter

        self._token_processor = TokenProcessor( ScopeWalker( self._target_adapter ) )

    def visit( self, input_source: Union[ TextIO, str ] ) -> None:
        """
        Walks the JSON input source.

        Parameters:
            `input_source`: the JSON input source. The input source is expected to be a file-like object or a string.

        Returns:
            None
        """

        self._token_processor.process( input_source )
