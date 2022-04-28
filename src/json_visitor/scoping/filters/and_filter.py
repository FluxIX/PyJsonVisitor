from .boolean_filter import BooleanFilter

class AndFilter( BooleanFilter ):
    def _get_short_circuit_comparison_value( self ) -> bool:
        return False

    def _boolean_operation( self, left_value: bool, right_value: bool ) -> bool:
        return left_value and right_value
