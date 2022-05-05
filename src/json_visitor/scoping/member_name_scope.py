__version__ = r"1.2.0"

from typing import Any, Dict, List, Iterable

from .scope_types import ScopeTypes
from .scope import Scope

class MemberNameScope( Scope ):
    """
    Implements a JSON member name node scope.
    """

    def __init__( self, name: str = None, parent: "MemberScope" = None ):
        super().__init__( ScopeTypes.MemberName, parent )

        self._name: str = name

    @property
    def name( self ) -> str:
        """
        The name of the member node.
        
        Returns:
            The name of the member node.
        """

        return self._name

    def get_value( self ) -> Any:
        """
        Gets the evaluated value of the current scope.

        Returns:
            The evaluated value of the current scope.
        """

        return self.name

    def _get_repr_param_strings( self ) -> List[ str ]:
        name_str: str = f"name = { repr( self.name ) }"
        parent_str: str = f"parent = { repr( None ) }"

        return [ name_str, parent_str ]

    def _get_str_param_strings( self ) -> List[ str ]:
        name_str: str = f"name = { f'{ self.name }' if self.name is not None else None }"

        return [ name_str ]

    def _get_children_scopes( self ) -> Iterable[ Scope ]:
        return tuple()

    def set_value( self, value: Any, **kwargs: Dict[ str, Any ] ) -> None:
        """
        Sets the value of the current scope to the given value.
        
        Parameters:
            `value`: the value the current scope is being set to.

        Returns:
            None
        """

        self._name = value
