__version__ = "1.0.0"

from typing import Any, Dict

from ..scope import Scope

try:
    from .filter_member_name import FilterMemberName
except ImportError:
    pass

from .value_filter import ValueFilter

class ValueComparisonFilter( ValueFilter ):
    """
    Implements a filter which selects based on a scope member's evaluated value as compared to another value.
    """

    def __init__( self, member_name: "FilterMemberName", comparison_source: Any ):
        super().__init__( member_name )

        self._comparison_source: Any = comparison_source

    @property
    def comparison_value( self ) -> Any:
        """
        The value the scope member's evaluated value is compared to.
        """

        return self._comparison_source

    def _internal_evaluate( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        return self._evalate_result( self.member_name.get_value( scope_item, **kwargs ), self.comparison_value, **kwargs )

    def _evalate_result( self, value: Any, comparison_value: Any, **kwargs: Dict[ str, Any ] ):
        raise NotImplementedError( "Child must implement." )
