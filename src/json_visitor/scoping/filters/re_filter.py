__version__ = "1.0.0"

from typing import Any, Dict, Union

import re
from ..scope import Scope

try:
    from .filter_member_name import FilterMemberName
except ImportError:
    pass

from .value_filter import ValueFilter

class RegularExpressionFilter( ValueFilter ):
    def __init__( self, member_name: "FilterMemberName", expression: Union[ str, re.Pattern ], **kwargs: Dict[ str, Any ] ):
        super().__init__( member_name )

        if isinstance( expression, str ):
            flags: int = kwargs.get( "expression_flags", None )
            if flags is not None:
                flags = int( flags )
            else:
                flags = 0

            expression = re.compile( expression, flags = flags )

        if isinstance( expression, re.Pattern ):
            self._expression: re.Pattern = expression
        else:
            raise ValueError( "Expression must be a regular expression Pattern." )

    @property
    def expression( self ) -> re.Pattern:
        return self._expression

    def _internal_evaluate( self, scope_item: Scope, **kwargs: Dict[ str, Any ] ) -> bool:
        value: Any = self.member_name.get_value( scope_item, **kwargs )
        if not isinstance( value, str ):
            raise ValueError( f"Invalid data type for regular expression matching; string is required." )
        else:
            return self._do_match( self.expression, value ) != None

    def _do_match( self, expression: re.Pattern, value: str ) -> re.Match:
        raise NotImplementedError( "Child must implement." )
