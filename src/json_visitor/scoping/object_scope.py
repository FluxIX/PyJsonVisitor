from typing import Any, Dict, Iterable, List
from .scope import Scope
from .member_scope import MemberScope

class ObjectScope( Scope ):
    """
    Implements a JSON object node scope.
    """

    def __init__( self, parent: Scope = None, member_scopes: Iterable[ MemberScope ] = None ):
        super().__init__( parent )

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
        """

        return self.members

    def _get_repr_param_strings( self ) -> List[ str ]:
        parent_str: str = f"parent = { repr( None ) }"
        member_scopes_str: str = f"member_scopes = { repr( self._member_scopes ) }"

        return [ parent_str, member_scopes_str ]

    def _get_str_param_strings( self ) -> List[ str ]:
        return [ f"members = { self.members }" ]
