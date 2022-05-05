__version__ = "1.0.0"

from typing import Any, Dict, Iterable, List

from ..scope import Scope
from .base_filter import BaseFilter

class BooleanFilter( BaseFilter ):
    def __init__( self, *filters: Iterable[ BaseFilter ], **kwargs: Dict[ str, Any ] ):
        for filter_ in filters:
            if not isinstance( filter_, BaseFilter ):
                raise ValueError( f"Filters must be a child of { BaseFilter.__qualname__ }" )

        self._filters: List[ BaseFilter ] = list( filters )

        self._short_circuit_evaluation: bool = bool( kwargs.get( "short_circuit_evaluation", True ) )

    @property
    def filters( self ) -> List[ BaseFilter ]:
        return self._filters

    @property
    def does_short_circuit_evaluation( self ) -> bool:
        return self._short_circuit_evaluation

    def _internal_evaluate( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        iterator = iter( self.filters )

        evaluated: bool = False
        result: bool = None
        try:
            while not evaluated:
                filter_: BaseFilter = next( iterator )
                result = filter_( scope_item, **kwargs )
                evaluated = self.does_short_circuit_evaluation and result == self._get_short_circuit_comparison_value()
        except StopIteration:
            pass
        finally:
            return result

    def _boolean_operation( self, left_value: bool, right_value: bool ) -> bool:
        """
        Returns `True` if the boolean operation is true for the given values, `False` otherwise.
        """

        raise NotImplementedError( "Child must implement." )

    def _get_short_circuit_comparison_value( self ) -> bool:
        """
        Returns the boolean value which the evaluation will short-circuit on.
        """

        raise NotImplementedError( "Child must implement." )
