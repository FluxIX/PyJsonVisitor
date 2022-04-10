from typing import Any, List
from ..scoping.scope import Scope
from ..scoping.root_scope import RootScope
from ..scoping.value_scope import ValueScope
from ..scoping.list_scope import ListScope
from ..scoping.list_item_scope import ListItemScope
from ..scoping.list_item_value_scope import ListItemValueScope
from ..scoping.object_scope import ObjectScope
from ..scoping.member_scope import MemberScope
from ..scoping.member_name_scope import MemberNameScope
from ..scoping.member_value_scope import MemberValueScope
from .base_adapter import BaseAdapter

class ScopeAdapter( BaseAdapter ):
    """
    An adapter which builds a scope chain for the visited document.
    """

    def __init__( self ):
        super().__init__()

        self.current_scope: Scope = None
        self._root: RootScope = None

        self._values: List[ Any ] = []
        self._list_item_scopes_stack: List[ List[ Any ] ] = []

    def get_current_scope( self ) -> Scope:
        """
        Gets the current scope or `None` if there is no current scope.
        """

        return self._current_scope

    def set_current_scope( self, value: Scope ) -> None:
        """
        Sets the current current scope to the given value.
        """

        self._current_scope: Scope = value

    current_scope = property( fget = get_current_scope, fset = set_current_scope )

    @property
    def root_scope( self ) -> RootScope:
        """
        Gets the root scope.
        
        Returns:
            The root scope.
        """

        return self._root

    @property
    def has_root_scope( self ) -> bool:
        """
        `True` if the adapter has a root scope, `False` otherwise.
        """

        return self._root is not None

    def _push_scope( self, scope: Scope ) -> None:
        """
        Sets the current scope to the given scope, linking the previous scope to it as its the parent.
        """

        if not self.has_root_scope:
            self._root = scope
        elif self.current_scope.is_root:
            self.root_scope._child = scope

        scope.parent = self.current_scope
        self.current_scope = scope

    def _pop_scope( self ) -> Scope:
        """
        Removes the last scope, unlinking it from its parent scope.
        
        Returns:
            The last scope which was removed.
        """

        if self.current_scope is None:
            raise ValueError( "Error popping scope: there is no scope to pop." )
        else:

            result = self.current_scope

            self.current_scope = self.current_scope.parent

            result.parent = None

            return result

    def before_document_start( self ) -> None:
        """
        Callback invoked before processing the start of the document.
        """

        super().before_document_start()

        self._push_scope( RootScope() )

    def after_document_end( self ) -> None:
        """
        Callback invoked after processing the end of the document.
        """

        super().after_document_end()

        self._pop_scope()

    def before_object_start( self ) -> None:
        """
        Callback invoked before processing the start of an object.
        """

        super().before_object_start()

        self._push_scope( ObjectScope() )

    def after_object_end( self ) -> None:
        """
        Callback invoked after processing the end of an object.
        """

        super().after_object_end()

        self._values.append( self.current_scope.get_value() )

        self._pop_scope()

    def before_member_start( self ) -> None:
        """
        Callback invoked before processing the start of a member.
        """

        super().before_member_start()

        scope = MemberScope()

        self.current_scope._member_scopes.append( scope )
        self._push_scope( scope )

    def after_member_end( self ) -> None:
        """
        Callback invoked after processing the end of a member.
        """

        super().after_member_end()

        self._pop_scope()

    def before_member_key( self, name: str ) -> None:
        """
        Callback invoked before processing the member key.
        
        Parameters:
            `name`: The member key.
        """

        super().before_member_key( name )

        scope = MemberNameScope( name )

        self.current_scope._name_scope = scope
        self._push_scope( scope )

    def after_member_key( self, name: str ) -> None:
        """
        Callback invoked after processing the member key.
        
        Parameters:
            `name`: The member key.
        """

        super().after_member_key( name )

        self._pop_scope()

    def before_member_value_start( self ) -> None:
        """
        Callback invoked before processing the start of a member value.
        """

        super().before_member_value_start()

        scope = MemberValueScope( is_initial_value = True )

        self.current_scope._value_scope = scope
        self._push_scope( scope )

    def after_member_value_end( self ) -> None:
        """
        Callback invoked after processing the end of a member value.
        """

        super().after_member_value_end()

        self.current_scope.set_value( self._values.pop() )

        self._pop_scope()

    def before_list_start( self ) -> None:
        """
        Callback invoked before processing the start of a list.
        """

        super().before_list_start()

        scope = ListScope()

        self.current_scope.value = scope
        self._push_scope( scope )

        self._list_item_scopes_stack.append( [] )

    def after_list_end( self ) -> None:
        """
        Callback invoked after processing the end of a list.
        """

        self.current_scope._item_scopes = self._list_item_scopes_stack.pop()

        super().after_list_end()

        self._values.append( self.current_scope.get_value() )

        self._pop_scope()

    def before_list_item_start( self ) -> None:
        """
        Callback invoked before processing the start of a list item.
        """

        super().before_list_item_start()

        scope = ListItemScope( item_index = len( self.current_scope.get_value() ) )

        self.current_scope._item_scopes.append( scope )
        self._push_scope( scope )
        self._list_item_scopes_stack[ -1 ].append( scope )

    def after_list_item_end( self ) -> None:
        """
        Callback invoked after processing the end of a list item.
        """

        super().after_list_item_end()

        self._pop_scope()

    def before_list_item_value_start( self ) -> None:
        """
        Callback invoked before processing the start of a list item value.
        """

        super().before_list_item_value_start()

        scope = ListItemValueScope( is_initial_value = True )

        self.current_scope._item_value_scope = scope
        self._push_scope( scope )

    def after_list_item_value_end( self ) -> None:
        """
        Callback invoked after processing the end of a list item value.
        """

        super().after_list_item_value_end()

        self.current_scope.set_value( self._values.pop() )

        self._pop_scope()

    def process_value( self, value: Any ) -> None:
        """
        Callback invoked when processing the value.

        Parameters:
            `value`: the value being processed.
        """

        super().process_value( value )

        if self.current_scope.is_root:
            # A value with a root scope as the parent indicates the JSON string does is a value, not a list or object.
            # Since a ValueScope can't have any children, no popping of the scope will be done.
            self._push_scope( ValueScope( initial_value = value ) )
        else:
            self._values.append( value )
