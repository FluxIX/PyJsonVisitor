__version__ = r"2.1.0"

from typing import List

from .scope_types import ScopeTypes
from .scope import Scope

class ValueScope( Scope ):
    """
    Implements a JSON value node scope.
    """

    def __init__( self, scope_type: ScopeTypes, parent: Scope = None ):
        super().__init__( scope_type, parent )

    def _get_str_param_strings( self ) -> List[ str ]:
        return [ f"value = { self.get_value() }" ]
