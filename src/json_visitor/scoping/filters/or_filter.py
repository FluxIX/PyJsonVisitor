from .boolean_filter import BooleanFilter

class OrFilter( BooleanFilter ):
    def _get_short_circuit_comparison_value( self ) -> bool:
        return True

    def _boolean_operation( self, left_value: bool, right_value: bool ) -> bool:
        return left_value or right_value
