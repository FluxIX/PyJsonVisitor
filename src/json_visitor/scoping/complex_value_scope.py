__version__ = "1.0.0"

from typing import Any, Dict, List, Iterable

from .scope_types import ScopeTypes
from .scope import Scope
from .value_scope import ValueScope

class ComplexValueScope( ValueScope ):
    def __init__( self, scope_type: ScopeTypes, child_scope: Scope, parent: Scope = None ):
        super().__init__( scope_type, parent )

        self._child: Scope = None
        self.set_child_scope( child_scope )

    @property
    def child_scope( self ) -> Scope:
        """
        The child scope for the current scope.

        Returns:
            The child scope for the current scope.
        """

        return self._child

    @property
    def has_child_scope( self ) -> bool:
        """
        Indicates if the current scope has a child scope.
        
        Returns:
            `True` if the current scope has a child scope, `False` otherwise.
        """

        return self.child_scope is not None

    def get_value( self ) -> Any:
        """
        Gets the evaluated value of the current scope.

        Returns:
            The evaluated value of the current scope.
        """

        if self.has_child_scope:
            return self.child_scope.get_value()
        else:
            raise ValueError( "Value scope has no child scope." )

    def _get_repr_param_strings( self ) -> List[ str ]:
        child_scope_str: str = f"child = { repr( self.child_scope ) }"

        return [ child_scope_str ]

    def _get_str_param_strings( self ) -> List[ str ]:
        return [ f"child = { self.child_scope }" ]

    def _get_children_scopes( self ) -> Iterable[ Scope ]:
        return ( self.child_scope, )

    def set_value( self, value: Any, **kwargs: Dict[ str, Any ] ) -> None:
        """
        Sets the value of the current scope to the given value.
        
        Parameters:
            `value`: the value the current scope is being set to.

        Returns:
            None
        """

        scope_tree: Scope = self._get_scope_tree( value, **kwargs )
        self.set_child_scope( scope_tree )

    def set_child_scope( self, child_scope: Scope ) -> None:
        """
        Sets the current scope's value scope to the given value scope.
        
        Parameters:
            `value_scope`: the value scope of the current scope is being set to.

        Returns:
            None
        """

        # TODO: consider a method which examines the current child before replacing it.

        if self.has_child_scope:
            self.child_scope.parent = None

        self._child: Scope = child_scope

        if self.has_child_scope:
            self.child_scope.set_parent( self )
