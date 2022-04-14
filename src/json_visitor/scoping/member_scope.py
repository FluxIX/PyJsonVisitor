__version__ = r"1.0.0"

from typing import Any, List

from .scope import Scope
from .member_name_scope import MemberNameScope
from .member_value_scope import MemberValueScope

class MemberScope( Scope ):
    """
    Implements a JSON member node scope.
    """

    def __init__( self, parent: "ObjectScope" = None, name_scope: MemberNameScope = None, value_scope: MemberValueScope = None ):
        super().__init__( parent )

        self._name_scope: MemberNameScope = name_scope
        self._value_scope: MemberValueScope = value_scope

    @property
    def name_scope( self ) -> MemberNameScope:
        """
        The name scope of the member node.
        
        Returns:
            The name scope of the member node.
        """

        return self._name_scope

    @property
    def has_name_scope( self ) -> bool:
        """
        Indicates if the member scope has a name scope.

        Returns:
            `True` if the member scope has a name scope, `False` otherwise.
        """

        return self.name_scope is not None

    @property
    def name( self ) -> str:
        """
        Gets the name of the current member.
        """

        if not self.has_name_scope:
            raise ValueError( "No member name scope." )
        else:
            return self.name_scope.get_value()

    @property
    def value_scope( self ) -> MemberValueScope:
        """
        The value scope of the member node.
        
        Returns:
            The value scope of the member node.
        """

        return self._value_scope

    @property
    def has_value_scope( self ) -> bool:
        """
        Indicates if the member scope has a value scope.

        Returns:
            `True` if the member scope has a value scope, `False` otherwise.
        """

        return self.value_scope is not None

    @property
    def value( self ) -> Any:
        """
        Gets the value of the current member scope.
        """

        if not self.has_value_scope:
            raise ValueError( "No member value scope." )
        else:
            return self.value_scope.get_value()

    def get_value( self ) -> Any:
        """
        Gets the evaluated value of the current scope.

        Returns:
            The evaluated value of the current scope.
        """

        return self.name, self.value

    def _get_repr_param_strings( self ) -> List[ str ]:
        parent_str: str = f"parent = { repr( None ) }"
        name_scope_str: str = f"name_scope = { repr( self.name_scope ) }"
        value_scope_str: str = f"value_scope = { repr( self.value_scope ) }"

        return [ parent_str, name_scope_str, value_scope_str ]

    def _get_str_param_strings( self ) -> List[ str ]:
        name_str: str = f"name = { f'{ self.name_scope.get_value() }' if self.name_scope is not None else None }"
        value_str: str = f"value = { self.value_scope.get_value() if self.value_scope is not None else None }"

        return [ name_str, value_str ]
