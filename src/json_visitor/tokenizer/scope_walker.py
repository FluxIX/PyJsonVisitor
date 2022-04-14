__version__ = r"1.0.0"

from typing import Any, Callable, Dict, Iterable, List, Tuple

from enum import Enum, auto
from ..simple_adapters.base_adapter import BaseAdapter

class ScopeTypes( Enum ):
    RootObject = auto()
    Object = auto()
    List = auto()
    ListItem = auto()
    ListItemValue = auto()
    Member = auto()
    MemberName = auto()
    MemberValue = auto()
    Value = auto()

class ScopeWalker( object ):
    # TODO: Update the order of execution documentation.
    """
    Walks the JSON file in a depth-first manner.

    Order of execution for a start node:
    1. Append current scope.
    3. All child scopes.
    2. "before_" callback.
    4. "process_" callback.
    5. "after_" callback.
    
    Order of execution for an end node:
    1. All child scopes.
    2. "before_" callback.
    3. "process_" callback.
    4. "after_" callback.
    5. Pop current scope.
    """

    def __init__( self, *adapters: Iterable[ BaseAdapter ] ):
        self._adapters: Tuple[ BaseAdapter ] = tuple( adapters )

        self._scope_stack: List[ ScopeTypes ] = []
        self._member_scope_initialization_stack = []

    @property
    def current_scope_type( self ) -> ScopeTypes:
        """
        Gets the current scope type.
        
        Returns:
            The current scope type. If there is no current scope, `None` is returned.
        """

        return self._scope_stack[ -1 ] if len( self._scope_stack ) > 0 else None

    def process_document_start( self ) -> None:
        self._scope_stack.append( ScopeTypes.RootObject )

        for adapter in self._adapters:
            adapter.before_document_start()

        for adapter in self._adapters:
            adapter.process_document_start()

        for adapter in self._adapters:
            adapter.after_document_start()

    def process_document_end( self ) -> None:
        for adapter in self._adapters:
            adapter.before_document_end()

        for adapter in self._adapters:
            adapter.process_document_end()

        for adapter in self._adapters:
            adapter.after_document_end()

        self._scope_stack.pop()

    def process_start_map( self, value: Any ) -> None:
        if self.current_scope_type == ScopeTypes.Member:
            self._process_member_value_start()
        elif self.current_scope_type == ScopeTypes.List:
            self._process_list_member_value_start()

        self._scope_stack.append( ScopeTypes.Object )

        for adapter in self._adapters:
            adapter.before_object_start()

        for adapter in self._adapters:
            adapter.process_object_start()

        for adapter in self._adapters:
            adapter.after_object_start()

    def process_end_map( self, value: Any ) -> None:
        for adapter in self._adapters:
            adapter.before_object_end()

        for adapter in self._adapters:
            adapter.process_object_end()

        for adapter in self._adapters:
            adapter.after_object_end()

        self._scope_stack.pop()

        if self.current_scope_type == ScopeTypes.MemberValue:
            self._process_member_value_end()
        elif self.current_scope_type == ScopeTypes.ListItemValue:
            self._process_list_member_value_end()

    def process_map_key( self, value: Any ) -> None:
        if not isinstance( value, str ):
            raise ValueError( f"Map key '{ value }' must be a string." )

        self._scope_stack.append( ScopeTypes.Member )

        for adapter in self._adapters:
            adapter.before_member_start()

        for adapter in self._adapters:
            adapter.process_member_start()

        for adapter in self._adapters:
            adapter.after_member_start()

        self._scope_stack.append( ScopeTypes.MemberName )

        for adapter in self._adapters:
            adapter.before_member_key( value )

        for adapter in self._adapters:
            adapter.process_member_key( value )

        for adapter in self._adapters:
            adapter.after_member_key( value )

        self._scope_stack.pop()

    def _process_member_value_start( self ) -> None:
        self._scope_stack.append( ScopeTypes.MemberValue )

        for adapter in self._adapters:
            adapter.before_member_value_start()

        for adapter in self._adapters:
            adapter.process_member_value_start()

        for adapter in self._adapters:
            adapter.after_member_value_start()

    def _process_member_value_end( self ) -> None:
        for adapter in self._adapters:
            adapter.before_member_value_end()

        for adapter in self._adapters:
            adapter.process_member_value_end()

        for adapter in self._adapters:
            adapter.after_member_value_end()

        self._scope_stack.pop()

        for adapter in self._adapters:
            adapter.before_member_end()

        for adapter in self._adapters:
            adapter.process_member_end()

        for adapter in self._adapters:
            adapter.after_member_end()

        self._scope_stack.pop()

    def process_start_array( self, value: Any ) -> None:
        if self.current_scope_type == ScopeTypes.Member:
            self._process_member_value_start()
        elif self.current_scope_type == ScopeTypes.List:
            self._process_list_member_value_start()

        self._scope_stack.append( ScopeTypes.List )

        for adapter in self._adapters:
            adapter.before_list_start()

        for adapter in self._adapters:
            adapter.process_list_start()

        for adapter in self._adapters:
            adapter.after_list_start()

    def process_end_array( self, value: Any ) -> None:
        for adapter in self._adapters:
            adapter.before_list_end()

        for adapter in self._adapters:
            adapter.process_list_end()

        for adapter in self._adapters:
            adapter.after_list_end()

        self._scope_stack.pop()

        if self.current_scope_type == ScopeTypes.MemberValue:
            self._process_member_value_end()
        elif self.current_scope_type == ScopeTypes.ListItemValue:
            self._process_list_member_value_end()

    def _process_list_member_value_start( self ) -> None:
        self._scope_stack.append( ScopeTypes.ListItem )

        for adapter in self._adapters:
            adapter.before_list_item_start()

        for adapter in self._adapters:
            adapter.process_list_item_start()

        for adapter in self._adapters:
            adapter.after_list_item_start()

        self._scope_stack.append( ScopeTypes.ListItemValue )

        for adapter in self._adapters:
            adapter.before_list_item_value_start()

        for adapter in self._adapters:
            adapter.process_list_item_value_start()

        for adapter in self._adapters:
            adapter.after_list_item_value_start()

    def _process_list_member_value_end( self ) -> None:
        for adapter in self._adapters:
            adapter.before_list_item_value_end()

        for adapter in self._adapters:
            adapter.process_list_item_value_end()

        for adapter in self._adapters:
            adapter.after_list_item_value_end()

        self._scope_stack.pop()

        for adapter in self._adapters:
            adapter.before_list_item_end()

        for adapter in self._adapters:
            adapter.process_list_item_end()

        for adapter in self._adapters:
            adapter.after_list_item_end()

        self._scope_stack.pop()

    def process_value( self, value: Any ) -> None:
        is_member_value: bool = self.current_scope_type == ScopeTypes.Member
        is_list_item_value: bool = self.current_scope_type == ScopeTypes.List

        if is_member_value:
            self._process_member_value_start()
        elif is_list_item_value:
            self._process_list_member_value_start()

        self._scope_stack.append( ScopeTypes.Value )

        for adapter in self._adapters:
            adapter.before_value( value )

        for adapter in self._adapters:
            adapter.process_value( value )

        for adapter in self._adapters:
            adapter.after_value( value )

        self._scope_stack.pop()

        if is_member_value:
            self._process_member_value_end()
        elif is_list_item_value:
            self._process_list_member_value_end()
