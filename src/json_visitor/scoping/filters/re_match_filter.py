__version__ = "1.0.0"

from typing import Any, Dict, Union

import re

try:
    from .filter_member_name import FilterMemberName
except ImportError:
    pass

from .re_filter import RegularExpressionFilter

class RegularExpressionMatchFilter( RegularExpressionFilter ):
    """
    Implements a filter which selects a scope by matching a scope's evaluated value against a regular expression using the `match` method.
    """

    def __init__( self, member_name: "FilterMemberName", expression: Union[ str, re.Pattern ], **kwargs: Dict[ str, Any ] ):
        super().__init__( member_name, expression, **kwargs )

    def _do_match( self, expression: re.Pattern, value: str ) -> re.Match:
        return expression.match( value )
