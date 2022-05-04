__version__ = r"1.2.0"

from typing import Any, Dict, List, Iterable

from .scope_types import ScopeTypes
from .scope import Scope
from .list_item_value_scope import ListItemValueScope

class ListItemScope( Scope ):
    """
    Implements a JSON list item scope.
    """

    def __init__( self, **kwargs: Dict[ str, Any ] ):
        parent: "ListScope" = kwargs.get( "parent", None )

        super().__init__( ScopeTypes.ListItem, parent )

        self._item_index: int = kwargs.get( "item_index", None )
        if self._item_index is not None:
            self._item_index: int = int( self._item_index )

        self._item_value_scope: ListItemValueScope = None
        self.set_value_scope( kwargs.get( "item_value_scope", None ) )

    @property
    def item_index( self ) -> int:
        """
        The list index of the current scope.

        Returns:
        The list index of the current scope.
        """

        return self._item_index

    @property
    def has_item_index( self ) -> bool:
        """
        Indicates if the current scope has an item index.
        
        Returns:
            `True` if the current scope has an item index, `False` otherwise.
        """

        return self.item_index is not None

    @property
    def item_value_scope( self ) -> ListItemValueScope:
        """
        The item value scope of the current scope.

        Returns:
            The item value scope of the current scope.
        """

        return self._item_value_scope

    @property
    def has_item_value_scope( self ) -> bool:
        """
        Indicates if the current scope has an item value scope.
        
        Returns:
            `True` if the current scope has an item value scope, `False` otherwise.
        """

        return self.item_value_scope is not None

    def get_value( self ) -> Any:
        """
        Gets the evaluated value of the current scope.

        Returns:
            The evaluated value of the current scope.
        """

        if self.has_item_value_scope:
            return self.item_value_scope.get_value()
        else:
            raise ValueError( "No list item value scope set." )

    def _get_repr_param_strings( self ) -> List[ str ]:
        parent_str: str = f"parent = { repr( None ) }"
        item_index_index_str: str = f"item_index = { self.item_index }"
        item_value_scope_str: str = f"item_value_scope = { repr( self.item_value_scope ) }"

        return [ parent_str, item_index_index_str, item_value_scope_str ]

    def _get_str_param_strings( self ) -> List[ str ]:
        return [ f"{ self.item_index }: { self.item_value_scope.get_value() if self.item_value_scope is not None else None }" ]

    def _get_children_scopes( self ) -> Iterable[ Scope ]:
        return ( self.item_value_scope, )

    def set_value( self, value: Any, **kwargs: Dict[ str, Any ] ) -> None:
        """
        Sets the evaluated value of the current scope.
        """

        scope_tree: Scope = self._get_scope_tree( value, **kwargs )
        self.set_value_scope( scope_tree )


    def set_value_scope( self, value_scope: Scope ) -> None:
        # TODO: consider a method which examines the current child before replacing it.

        if self.has_item_value_scope:
            self.item_value_scope.parent = None

        self._item_value_scope: ListItemValueScope = value_scope

        if self.has_item_value_scope:
            self.item_value_scope.set_parent( self )
