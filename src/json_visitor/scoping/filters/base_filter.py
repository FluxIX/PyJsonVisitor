from typing import Any, Dict

from ..scope import Scope

class BaseFilter( object ):
    def __call__( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        if scope_item is None:
            raise ValueError( "Scope item cannot be None." )
        else:
            return self._internal_evaluate( scope_item, **kwargs )

    def _internal_evaluate( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        raise NotImplementedError( "Child must implement." )

    def and_( self, other: "BaseFilter", **kwargs: Dict[ str, Any ] ) -> "AndFilter":
        from .and_filter import AndFilter

        self_is_and: bool = isinstance( self, AndFilter )
        other_is_and: bool = isinstance( other, AndFilter )

        if self_is_and:
            if other_is_and:
                self.filters.extend( other.filters )
            else:
                self.filters.append( other )

            result = self
        else:
            if other_is_and:
                other.filters.insert( 0, self )
                result = other
            else:
                result = AndFilter( self, other, **kwargs )

        return result

    def or_( self, other: "BaseFilter", **kwargs: Dict[ str, Any ] ) -> "OrFilter":
        from .and_filter import AndFilter
        from .or_filter import OrFilter

        other_is_and: bool = isinstance( other, AndFilter )
        self_is_or: bool = isinstance( self, OrFilter )
        other_is_or: bool = isinstance( other, OrFilter )

        if self_is_or:
            if other_is_or:
                self.filters.extend( other.filters )
                result = self
            elif other_is_and:
                other.filters.insert( 0, self )
                result = other
            else:
                self.filters.append( other )
                result = self
        else:
            result = OrFilter( self, other, **kwargs )

        return result

    def __invert__( self ) -> "BaseFilter":
        from .negation_filter import NegationFilter

        if isinstance( self, NegationFilter ):
            result: "BaseFilter" = self.filter_
        else:
            result: NegationFilter = NegationFilter( self )

        return result
