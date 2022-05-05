__version__ = "1.0.0"

from typing import Any, Dict, Iterable, Tuple

from ..scope import Scope
from .contains_filter import ContainsFilter

class InFilter( ContainsFilter ):
    """
    Implements a filter which selects a scope of the scope's evaluated value is in a set of given values.
    """

    def _internal_evaluate( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        value: Any = self.member_name.get_value( scope_item, **kwargs )
        return self._evaluate_value( [ value ], **kwargs )
