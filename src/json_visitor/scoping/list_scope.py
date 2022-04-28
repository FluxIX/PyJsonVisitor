__version__ = r"1.1.0"

from typing import Any, Iterable, List, Tuple

from .scope_types import ScopeTypes
from .scope import Scope
from .list_item_scope import ListItemScope

class ListScope( Scope ):
    """
    Implements a JSON list scope.
    """

    def __init__( self, parent: Scope = None, item_scopes: Iterable[ ListItemScope ] = None ):
        super().__init__( ScopeTypes.List, parent )

        if item_scopes is None:
            item_scopes: List[ ListItemScope ] = []

        self._item_scopes: List[ ListItemScope ] = list( item_scopes )

    @property
    def item_pairs( self ) -> Tuple[ Tuple[ int, Any ] ]:
        """
        The tuple of index-item tuples in the list.
        
        Returns:
            The tuple of the index-item tuples in the list.
        """

        return tuple( map( lambda scope: ( scope.item_index, scope.item_value_scope.get_value() ), self._item_scopes ) )

    @property
    def items( self ) -> Tuple[ Any ]:
        """
        The tuple of the items in the list.
        
        Returns:
            The tuple of the items in the list.
        """

        return tuple( map( lambda scope: scope.item_value_scope.get_value(), self._item_scopes ) )

    def get_value( self ) -> Any:
        """
        Gets the evaluated value of the current scope.

        Returns:
            The evaluated value of the current scope.
        """

        return self.items

    def _get_repr_param_strings( self ) -> List[ str ]:
        parent_str: str = f"parent = { repr( None ) }"
        items_str: str = f"item_scopes = { repr( self._item_scopes ) }"

        return [ parent_str, items_str ]

    def _get_str_param_strings( self ) -> List[ str ]:
        items_str: str = f"items = { self.get_value() }"

        return [ items_str ]

    def _get_children_scopes( self ) -> Iterable[ Scope ]:
        return tuple( self._item_scopes )
