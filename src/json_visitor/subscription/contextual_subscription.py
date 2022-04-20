__version__ = r"2.0.0"

from typing import Any, Iterable, List, Tuple

from ..scoping.root_scope import RootScope
from ..scoping.object_scope import ObjectScope
from ..scoping.member_scope import MemberScope
from ..scoping.list_scope import ListScope
from ..scoping.list_item_scope import ListItemScope
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

    def before_document( self, scope: RootScope, value: Any ) -> None:
        super().before_document( scope, value )

        self._event_notifier.raise_event( "before_document", scope, value )

    def process_document( self, scope: RootScope, value: Any ) -> None:
        super().process_document( scope, value )

        self._event_notifier.raise_event( "process_document", scope, value )

    def after_document( self, scope: RootScope, value: Any ) -> None:
        super().after_document( scope, value )

        self._event_notifier.raise_event( "after_document", scope, value )

    def before_object( self, scope: ObjectScope, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        super().before_object( scope, members )

        self._event_notifier.raise_event( "before_object", scope, members )

    def process_object( self, scope: ObjectScope, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        super().process_object( scope, members )

        self._event_notifier.raise_event( "process_object", scope, members )

    def after_object( self, scope: ObjectScope, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        super().after_object( scope, members )

        self._event_notifier.raise_event( "after_object", scope, members )

    def before_member( self, scope: MemberScope, name: str, value: Any ) -> None:
        super().before_member( scope, name, value )

        self._event_notifier.raise_event( "before_member", scope, name, value )

    def process_member( self, scope: MemberScope, name: str, value: Any ) -> None:
        super().process_member( scope, name, value )

        self._event_notifier.raise_event( "process_member", scope, name, value )

    def after_member( self, scope: MemberScope, name: str, value: Any ) -> None:
        super().after_member( scope, name, value )

        self._event_notifier.raise_event( "after_member", scope, name, value )

    def before_list( self, scope: ListScope, items: Iterable[ Any ] ) -> None:
        super().before_list( scope, items )

        self._event_notifier.raise_event( "before_list", scope, items )

    def process_list( self, scope: ListScope, items: Iterable[ Any ] ) -> None:
        super().process_list( scope, items )

        self._event_notifier.raise_event( "process_list", scope, items )

    def after_list( self, scope: ListScope, items: Iterable[ Any ] ) -> None:
        super().after_list( scope, items )

        self._event_notifier.raise_event( "after_list", scope, items )

    def before_list_item( self, scope: ListItemScope, index_: int, value: Any ) -> None:
        super().before_list_item( scope, index_, value )

        self._event_notifier.raise_event( "before_list_item", scope, index_, value )

    def process_list_item( self, scope: ListItemScope, index_: int, value: Any ) -> None:
        super().process_list_item( scope, index_, value )

        self._event_notifier.raise_event( "process_list_item", scope, index_, value )

    def after_list_item( self, scope: ListItemScope, index_: int, value: Any ) -> None:
        super().after_list_item( scope, index_, value )

        self._event_notifier.raise_event( "after_list_item", scope, index_, value )
