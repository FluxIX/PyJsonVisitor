__version__ = r"1.2.0"

from .scope_types import ScopeTypes
from .scope import Scope
from .complex_value_scope import ComplexValueScope

class ListItemValueScope( ComplexValueScope ):
    """
    Implements a JSON list item value node scope.
    """

    def __init__( self, value_scope: Scope = None, parent: "ListItemScope" = None ):
        super().__init__( ScopeTypes.ListItemValue, value_scope, parent )
