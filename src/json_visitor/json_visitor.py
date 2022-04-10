from typing import Union, TextIO

from .simple_adapters.base_adapter import BaseAdapter
from .tokenizer.scope_walker import ScopeWalker
from .tokenizer.token_processor import TokenProcessor

class JsonVisitor( object ):
    """
    Implements a visitor for JSON nodes in a JSON object using the Visitor pattern: https://en.wikipedia.org/wiki/Visitor_pattern.
    """

    def __init__( self, adapter: BaseAdapter ):
        if not isinstance( adapter, BaseAdapter ):
            raise ValueError( f"Adapter must be an instance of { BaseAdapter.__qualname__ }." )
        else:
            self._target_adapter: BaseAdapter = adapter

        self._token_processor = TokenProcessor( ScopeWalker( self._target_adapter ) )

    def walk( self, input_source: Union[ TextIO, str ] ) -> None:
        """
        Walks the JSON input source; the input source is expected to be a file-like object or a string and containing a root-level object.

        Notes:
            - Content in the input_source must represent a JSON object. Root-level integers and strings will result in a ValueError, but an array will result in erroroneous key-value pairs of list index -> value.
        """

        self._token_processor.process( input_source )
