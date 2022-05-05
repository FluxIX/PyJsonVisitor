from typing import Any, Dict, Iterable, Tuple

from ..scope import Scope
from .contains_filter import ContainsFilter

class InFilter( ContainsFilter ):
    def _internal_evaluate( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        value: Any = self.member_name.get_value( scope_item, **kwargs )
        return self._evaluate_value( [ value ], **kwargs )
