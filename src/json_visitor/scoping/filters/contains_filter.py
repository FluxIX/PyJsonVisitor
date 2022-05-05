__version__ = "1.0.0"

from typing import Any, Dict, Iterable, Tuple

from collections.abc import Iterable as Iterable_
from ..scope import Scope

try:
    from .filter_member_name import FilterMemberName
except ImportError:
    pass

from .value_filter import ValueFilter

class ContainsFilter( ValueFilter ):
    def __init__( self, member_name: "FilterMemberName", *values: Iterable[ Any ], **kwargs: Dict[ str, Any ] ):
        super().__init__( member_name )

        self._values: Tuple[ Any ] = tuple( values )

    def _internal_evaluate( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        return self._evaluate_value( self.member_name.get_value( scope_item, **kwargs ), **kwargs )

    def _evaluate_value( self, value: Iterable_, **kwargs: Dict[ str, Any ] ) -> bool:
        if isinstance( value, Iterable_ ):
            result: bool = False
            iterator = iter( self._values )
            while not result:
                try:
                    match_value: Any = next( iterator )
                except StopIteration:
                    break
                else:
                    result = match_value in value

            return result
        else:
            raise ValueError( f"Member value '{ self.member_name.member_name }' must be iterable." )
