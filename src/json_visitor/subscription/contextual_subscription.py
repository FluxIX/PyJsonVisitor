from typing import Any, Iterable, List, Tuple
from ..scoping.root_scope import RootScope
from .simple_subscription import SimpleSubscription
from ..contextual_adapters.base_adapter import BaseAdapter

class ContextualSubscription( BaseAdapter, SimpleSubscription ):
    def _get_subscription_keys( self ) -> List[ str ]:
        result: List[ str ] = super()._get_subscription_keys()
        result.extend( [ "before_document", "process_document", "after_document",
                         "before_object", "process_object", "after_object",
                         "before_member", "process_member", "after_member",
                         "before_list", "process_list", "after_list",
                         "before_list_item", "process_list_item", "after_list_item", ] )
        return result

    def before_document( self, root_scope: RootScope ) -> None:
        super().before_document( root_scope )

        self._event_notifier.raise_event( "before_document", root_scope )

    def process_document( self, root_scope: RootScope ) -> None:
        super().process_document( root_scope )

        self._event_notifier.raise_event( "process_document", root_scope )

    def after_document( self, root_scope: RootScope ) -> None:
        super().after_document( root_scope )

        self._event_notifier.raise_event( "after_document", root_scope )

    def before_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        super().before_object( members )

        self._event_notifier.raise_event( "before_object", members )

    def process_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        super().process_object( members )

        self._event_notifier.raise_event( "process_object", members )

    def after_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        super().after_object( members )

        self._event_notifier.raise_event( "after_object", members )

    def before_member( self, name: str, value: Any ) -> None:
        super().before_member( name, value )

        self._event_notifier.raise_event( "before_member", name, value )

    def process_member( self, name: str, value: Any ) -> None:
        super().process_member( name, value )

        self._event_notifier.raise_event( "process_member", name, value )

    def after_member( self, name: str, value: Any ) -> None:
        super().after_member( name, value )

        self._event_notifier.raise_event( "after_member", name, value )

    def before_list( self, items: Iterable[ Any ] ) -> None:
        super().before_list( items )

        self._event_notifier.raise_event( "before_list", items )

    def process_list( self, items: Iterable[ Any ] ) -> None:
        super().process_list( items )

        self._event_notifier.raise_event( "process_list", items )

    def after_list( self, items: Iterable[ Any ] ) -> None:
        super().after_list( items )

        self._event_notifier.raise_event( "after_list", items )

    def before_list_item( self, index_: int, value: Any ) -> None:
        super().before_list_item( index_, value )

        self._event_notifier.raise_event( "before_list_item", index_, value )

    def process_list_item( self, index_: int, value: Any ) -> None:
        super().process_list_item( index_, value )

        self._event_notifier.raise_event( "process_list_item", index_, value )

    def after_list_item( self, index_: int, value: Any ) -> None:
        super().after_list_item( index_, value )

        self._event_notifier.raise_event( "after_list_item", index_, value )
