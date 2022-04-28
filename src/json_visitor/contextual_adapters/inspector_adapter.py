__version__ = r"2.0.0"

from typing import Any, Dict, Iterable, Tuple

from ..scoping.root_scope import RootScope
from ..scoping.object_scope import ObjectScope
from ..scoping.member_scope import MemberScope
from ..scoping.list_scope import ListScope
from ..scoping.list_item_scope import ListItemScope
from .base_adapter import BaseAdapter
from ..simple_adapters.scope_inspector_adapter import ScopeInspectionAdapter

class InspectionAdapter( BaseAdapter, ScopeInspectionAdapter ):
    def __init__( self, **kwargs: Dict[ str, Any ] ):
        """
        Creates a InspectionAdapter.
        
        Keyword Arguments:
            `output_targets`: iterable of output targets.
            `open_file_mode`: file mode output targets will be opened with; defaults to write ("w").
            `output_console`: boolean which controls if stdout should be written to; defaults to True, indicating stdout will be written to.
            `output_error`: boolean which controls if stderr should be written to; defaults to False, indicating stderr will not be written to.
        """

        super().__init__( **kwargs )

    def process_document( self, scope: RootScope, value: Any ) -> None:
        super().process_document( scope, value )

        self._print_message( "process_document", scope.get_value() )

    def process_list( self, scope: ListScope, items: Iterable[ Any ] ) -> None:
        super().process_list( scope, items )

        self._print_message( "process_list", items )

    def process_list_item( self, scope: ListItemScope, index_: int, value: Any ) -> None:
        super().process_list_item( scope, index_, value )

        self._print_message( "process_list_item", index_, value )

    def process_object( self, scope: ObjectScope, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        super().process_object( scope, members )

        self._print_message( "process_object", members )

    def process_member( self, scope: MemberScope, name: str, value: Any ) -> None:
        super().process_member( scope, name, value )

        self._print_message( "process_member", name, value )
