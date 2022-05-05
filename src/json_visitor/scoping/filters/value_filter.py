__version__ = "1.0.0"

from typing import Any, Dict

from .base_filter import BaseFilter

class ValueFilter( BaseFilter ):
    """
    Implements a scope filter which has member name.
    """

    def __init__( self, member_name: "FilterMemberName" ):
        from .filter_member_name import FilterMemberName

        if not isinstance( member_name, FilterMemberName ):
            raise ValueError( f"Member name must be { FilterMemberName.__qualname__ }." )
        else:
            self._member_name = member_name

    @property
    def member_name( self ) -> "FilterMemberName":
        """
        The filter's member name.
        """

        return self._member_name
