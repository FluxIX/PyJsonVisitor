__version__ = r"1.2.0"

from typing import Any, Dict

from .scope_types import ScopeTypes
from .scope import Scope
from .complex_value_scope import ComplexValueScope

class RootScope( ComplexValueScope ):
    """
    Implements a JSON root node scope.
    """

    def __init__( self, child: Scope = None ):
        super().__init__( ScopeTypes.Root, child, None )

    def set_value( self, value: Any, **kwargs: Dict[ str, Any ] ) -> None:
        """
        Sets the evaluated value of the current scope.
        """

        raise NotImplementedError( "Unsupported operation." )
