__version__ = r"1.0.0"

from typing import Any

from .value_scope import ValueScope

class MemberValueScope( ValueScope ):
    """
    Implements a JSON member value node scope.
    """

    def __init__( self, parent: "MemberScope" = None, initial_value: Any = None, is_initial_value: bool = False ):
        super().__init__( parent, initial_value, is_initial_value )
