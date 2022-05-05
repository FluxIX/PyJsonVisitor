__version__ = "1.0.0"

from typing import Any, Dict, Iterable

from ..scope import Scope

class BaseFilter( object ):
    def __call__( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        if scope_item is None:
            raise ValueError( "Scope item cannot be None." )
        else:
            return self._internal_evaluate( scope_item, **kwargs )

    def _internal_evaluate( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        raise NotImplementedError( "Child must implement." )

    def and_( self, *others: Iterable[ "BaseFilter" ], **kwargs: Dict[ str, Any ] ) -> "AndFilter":
        from .and_filter import AndFilter

        result = self

        for other in others:
            result_is_and: bool = isinstance( result, AndFilter )
            other_is_and: bool = isinstance( other, AndFilter )

            if result_is_and:
                if other_is_and:
                    result.filters.extend( other.filters )
                else:
                    result.filters.append( other )
            else:
                if other_is_and:
                    other.filters.insert( 0, result )
                    result = other
                else:
                    result = AndFilter( result, other, **kwargs )

        return result

    def or_( self, *others: Iterable[ "BaseFilter" ], **kwargs: Dict[ str, Any ] ) -> "OrFilter":
        from .and_filter import AndFilter
        from .or_filter import OrFilter

        result = self

        for other in others:
            other_is_and: bool = isinstance( other, AndFilter )
            result_is_or: bool = isinstance( result, OrFilter )
            other_is_or: bool = isinstance( other, OrFilter )

            if result_is_or:
                if other_is_or:
                    result.filters.extend( other.filters )
                elif other_is_and:
                    other.filters.insert( 0, result )
                    result = other
                else:
                    result.filters.append( other )
            else:
                result = OrFilter( result, other, **kwargs )

        return result

    def __invert__( self ) -> "BaseFilter":
        from .negation_filter import NegationFilter

        if isinstance( self, NegationFilter ):
            result: "BaseFilter" = self.filter_
        else:
            result: NegationFilter = NegationFilter( self )

        return result
