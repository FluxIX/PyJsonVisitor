__version__ = r"2.0.0"

from .scope_types import ScopeTypes
from .scope import Scope
from .complex_value_scope import ComplexValueScope

class MemberValueScope( ComplexValueScope ):
    """
    Implements a JSON member value node scope.
    """

    def __init__( self, child_scope: Scope = None, parent: "MemberScope" = None ):
        super().__init__( ScopeTypes.MemberValue, child_scope, parent )
