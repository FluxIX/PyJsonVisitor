from typing import Any, Iterable, Tuple
from ..scoping.root_scope import RootScope
from .base_adapter import BaseAdapter
from ..simple_adapters.scope_inspector_adapter import ScopeInspectionAdapter

class InspectionAdapter( BaseAdapter, ScopeInspectionAdapter ):
    def process_document( self, root_scope: RootScope ) -> None:
        super().process_document( root_scope )

        self._print_message( "process_document", root_scope.get_value() )

    def process_list( self, items: Iterable[Any] ) -> None:
        super().process_list( items )

        self._print_message( "process_list", items )

    def process_list_item( self, index_: int, value: Any ) -> None:
        super().process_list_item( index_, value )

        self._print_message( "process_list_item", index_, value )

    def process_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        super().process_object( members )

        self._print_message( "process_object", members )

    def process_member( self, name: str, value: Any ) -> None:
        super().process_member( name, value )

        self._print_message( "process_member", name, value )
