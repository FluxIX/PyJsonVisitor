__version__ = r"1.1.0"

from typing import Any

from .scope_types import ScopeTypes
from .value_scope import ValueScope

class ListItemValueScope( ValueScope ):
    """
    Implements a JSON list item value node scope.
    """

    def __init__( self, parent: "ListItemScope" = None, initial_value: Any = None, is_initial_value: bool = False ):
        super().__init__( ScopeTypes.ListItemValue, parent, initial_value, is_initial_value )
