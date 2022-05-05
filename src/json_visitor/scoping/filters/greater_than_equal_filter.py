__version__ = "1.0.0"

from typing import Any, Dict

try:
    from .filter_member_name import FilterMemberName
except ImportError:
    pass

from .value_comparison_filter import ValueComparisonFilter

class GreaterThanEqualFilter( ValueComparisonFilter ):
    def __init__( self, member_name: "FilterMemberName", comparison_source: Any ):
        super().__init__( member_name, comparison_source )

    def _evalate_result( self, value: Any, comparison_value: Any, **kwargs: Dict[ str, Any ] ):
        return value >= comparison_value
