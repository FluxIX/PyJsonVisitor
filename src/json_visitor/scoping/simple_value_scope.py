__version__ = r"1.0.0"

from typing import Any

from .scope_types import ScopeTypes
from .scope import Scope
from .value_scope import ValueScope

class SimpleValueScope( ValueScope ):
    """
    Implements a JSON simple value node scope.
    """

    def __init__( self, parent: Scope = None, initial_value: Any = None, is_initial_value: bool = False ):
        super().__init__( ScopeTypes.SimpleValue, parent, initial_value, is_initial_value )
