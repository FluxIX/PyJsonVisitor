from .base_filter import BaseFilter

class NegationFilter( BaseFilter ):
    def __init__( self, filter_: BaseFilter ):
        if filter is None:
            raise ValueError( "Filter cannot be None." )
        else:
            self._filter: BaseFilter = filter_

    @property
    def filter_( self ) -> BaseFilter:
        return self._filter

    def _internal_evaluate( self, scope_item, **kwargs ) -> bool:
        return not self.filter_( scope_item, **kwargs )
