__version__ = r"1.2.0"

from typing import Any, Dict, Iterable, List

from .scope_types import ScopeTypes
from .scope import Scope
from .member_scope import MemberScope

class ObjectScope( Scope ):
    """
    Implements a JSON object node scope.
    """

    def __init__( self, parent: Scope = None, member_scopes: Iterable[ MemberScope ] = None ):
        super().__init__( ScopeTypes.Object, parent )

        if member_scopes is None:
            member_scopes = []

        self._member_scopes: List[ MemberScope ] = list( member_scopes )

    @property
    def members( self ) -> Dict[ str, Any ]:
        """
        The list of the members in the list.
        
        Returns:
            The list of the members in the list.
        """

        return dict( map( lambda scope: scope.get_value(), self._member_scopes ) )

    def get_value( self ) -> Any:
        """
        Gets the evaluated value of the current scope.

        Returns:
            The evaluated value of the current scope.
        """

        return self.members

    def _get_repr_param_strings( self ) -> List[ str ]:
        parent_str: str = f"parent = { repr( None ) }"
        member_scopes_str: str = f"member_scopes = { repr( self._member_scopes ) }"

        return [ parent_str, member_scopes_str ]

    def _get_str_param_strings( self ) -> List[ str ]:
        return [ f"members = { self.members }" ]

    def _get_children_scopes( self ) -> Iterable[ Scope ]:
        return tuple( self._member_scopes )

    def set_value( self, value: Any, **kwargs: Dict[ str, Any ] ) -> None:
        if not isinstance( value, dict ):
            raise ValueError( "Object scope value must be a dict." )
        else:
            # TODO: Consider a less-naive method.
            # A method which might work "better" would include sorting the keys and doing the following:
            #    - adding the new keys which did not previously exist
            #    - remove the keys which no longer exist
            #    - update existing keys with the new value; this could be recursive

            scope: ObjectScope = self._get_scope_tree( value )

            member_scopes: List[ MemberScope ] = scope._member_scopes

            for scope in self._member_scopes:
                scope.parent = None

            self._member_scopes = member_scopes

            for scope in self._member_scopes:
                scope.set_parent( self )
