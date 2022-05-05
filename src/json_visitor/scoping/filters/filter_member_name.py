__version__ = "1.0.0"

from typing import Any, Dict, Union, Iterable

import re
from ..scope import Scope
from .base_filter import BaseFilter
from .equality_filter import EqualityFilter
from .inequality_filter import InequalityFilter
from .less_than_filter import LessThanFilter
from .less_than_equal_filter import LessThanEqualFilter
from .greater_than_filter import GreaterThanFilter
from .greater_than_equal_filter import GreaterThanEqualFilter
from .re_match_filter import RegularExpressionMatchFilter
from .re_fullmatch_filter import RegularExpressionFullMatchFilter
from .re_search_filter import RegularExpressionSearchFilter
from .contains_filter import ContainsFilter
from .in_filter import InFilter

class FilterMemberName( object ):
    def __init__( self, member_name: str ):
        if not isinstance( member_name, str ):
            raise ValueError( "Member name must be string." )
        else:
            name: str = member_name.strip()
            if len( name ) > 0:
                self._member_name = member_name
            else:
                raise ValueError( "Member name cannot be an empty string." )

    @property
    def member_name( self ) -> str:
        return self._member_name

    def get_value( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> Any:
        if hasattr( scope_item, self.member_name ):
            return getattr( scope_item, self.member_name )
        else:
            raise ValueError( f"Scope does not have the '{ self.member_name }' member." )

    def __eq__( self, comparison_value: Any ) -> BaseFilter:
        return EqualityFilter( self, comparison_value )

    def __ne__( self, comparison_value: Any ) -> BaseFilter:
        return InequalityFilter( self, comparison_value )

    def __le__( self, comparison_value: Any ) -> BaseFilter:
        return LessThanEqualFilter( self, comparison_value )

    def __lt__( self, comparison_value: Any ) -> BaseFilter:
        return LessThanFilter( self, comparison_value )

    def __ge__( self, comparison_value: Any ) -> BaseFilter:
        return GreaterThanEqualFilter( self, comparison_value )

    def __gt__( self, comparison_value: Any ) -> BaseFilter:
        return GreaterThanFilter( self, comparison_value )

    def in_( self, *values: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> BaseFilter:
        """
        Creates a filter which selects a scope whose values which exist in the given values.
        
        Parameters:
            `values`: Iterable values which are used to verify the scope whose value is a member of.
            
        Returns:
            A filter which selects a scope whose values which exist in the given values.
        """

        return InFilter( self, *values, **kwargs )

    def contains( self, *values: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> BaseFilter:
        """
        Creates a filter which selects a scope which contains at least one value which exists in the given values.
        
        Parameters:
            `values`: Iterable values which are used to verify the scope which contains at least one value.
            
        Returns:
            A filter which selects a scope which contains at least one value which exists in the given values.
        """

        return ContainsFilter( self, *values, **kwargs )

    def re_matches( self, expression: Union[ str, re.Pattern ], **kwargs: Dict[ str, Any ] ) -> BaseFilter:
        """
        Creates a filter which selects a scope whose value matches the given regular expression (using the expression's `match` method).

        Parameters:
            `expression`: regular expression to match the scope's value against.
            
        Returns:
            A filter which selects a scope whose value matches the given regular expression (using the expression's `match` method).
        """

        return RegularExpressionMatchFilter( self, expression, **kwargs )

    def re_fullmatches( self, expression: Union[ str, re.Pattern ], **kwargs: Dict[ str, Any ] ) -> BaseFilter:
        """
        Creates a filter which selects a scope whose value matches the given regular expression (using the expression's `fullmatch` method).

        Parameters:
            `expression`: regular expression to match the scope's value against.
            
        Returns:
            A filter which selects a scope whose value matches the given regular expression (using the expression's `fullmatch` method).
        """

        return RegularExpressionFullMatchFilter( self, expression, **kwargs )

    def re_searches( self, expression: Union[ str, re.Pattern ], **kwargs: Dict[ str, Any ] ) -> BaseFilter:
        """
        Creates a filter which selects a scope whose value matches the given regular expression (using the expression's `search` method).

        Parameters:
            `expression`: regular expression to match the scope's value against.
            
        Returns:
            A filter which selects a scope whose value matches the given regular expression (using the expression's `search` method).
        """

        return RegularExpressionSearchFilter( self, expression, **kwargs )
