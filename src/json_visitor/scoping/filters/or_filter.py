__version__ = "1.0.0"

from .boolean_filter import BooleanFilter

class OrFilter( BooleanFilter ):
    """
    Implements a scope filter which selects a scope where at least one of the constituent filters evaluate to `True`.
    """

    def _get_short_circuit_comparison_value( self ) -> bool:
        return True

    def _boolean_operation( self, left_value: bool, right_value: bool ) -> bool:
        return left_value or right_value
