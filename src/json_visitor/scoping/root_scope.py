__version__ = r"1.1.0"

from typing import Any, List, Dict, Iterable

from .scope_types import ScopeTypes
from .scope import Scope

class RootScope( Scope ):
    """
    Implements a JSON root node scope.
    """

    def __init__( self, child: Scope = None ):
        super().__init__( ScopeTypes.Root, None )

        self._child: Scope = child

    @property
    def child_scope( self ) -> Scope:
        """
        The child scope for the current root scope.

        Returns:
            The child scope for the current root scope.
        """

        return self._child

    @property
    def has_child_scope( self ) -> bool:
        """
        Indicates if the current root scope has a child scope.
        
        Returns:
            `True` if the current root scope has a child scope, `False` otherwise.
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
            raise ValueError( "Root has no child scope." )

    def _get_repr_param_strings( self ) -> List[ str ]:
        child_scope_str: str = f"child = { repr( self.child_scope ) }"

        return [ child_scope_str ]

    def _get_str_param_strings( self ) -> List[ str ]:
        return [ f"child = { self.child_scope }" ]
