from typing import Any, Callable, Dict, Iterable, List, FrozenSet
from EventNotifier import Notifier
from ..simple_adapters.base_adapter import BaseAdapter

class SimpleSubscription( BaseAdapter ):
    def __init__( self ):
        self._subscription_keys: FrozenSet[ str ] = frozenset( self._get_subscription_keys() )

        self._event_notifier: Notifier = Notifier( self.subscription_keys )

    def _get_subscription_keys( self ) -> List[ str ]:
        """
        Gets the list of valid subscription keys.

        Returns:
            The list of valid subscription keys.
        """

        return [
            "default_before", "default_process", "default_after",
            "before_document_start", "process_document_start", "after_document_start",
            "before_document_end", "process_document_end", "after_document_end",
            "before_object_start", "process_object_start", "after_object_start",
            "before_object_end", "process_object_end", "after_object_end",
            "before_list_start", "process_list_start", "after_list_start",
            "before_list_end", "process_list_end", "after_list_end",
            "before_list_item_start", "process_list_item_start", "after_list_item_start",
            "before_list_item_end", "process_list_item_end", "after_list_item_end",
            "before_list_item_value_start", "process_list_item_value_start", "after_list_item_value_start",
            "before_list_item_value_end", "process_list_item_value_end", "after_list_item_value_end",
            "before_member_start", "process_member_start", "after_member_start",
            "before_member_end", "process_member_end", "after_member_end",
            "before_member_key", "process_member_key", "after_member_key",
            "before_member_value_start", "process_member_value_start", "after_member_value_start",
            "before_member_value_end", "process_member_value_end", "after_member_value_end",
            "before_value", "process_value", "after_value",
        ]

    @property
    def subscription_keys( self ) -> FrozenSet[ str ]:
        """
        The set of subscription keys.
        
        Returns:
            The set of subscription keys.
        """

        return self._subscription_keys

    def register( self, subscription_key: str, callback: Callable ) -> None:
        """
        Registers the given callback for the subscription associated with the given subscription key.

        Arguments:
            `subscription_key`: the key identifying the subscription.
            `callback`: the callback invoked when the event is triggered.
        """

        if subscription_key not in self.subscription_keys:
            raise ValueError( f"'{ subscription_key }' is not a valid key." )
        else:
            self._event_notifier.subscribe( subscription_key, callback )

    def default_before( self, *args: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> None:
        super().default_before( *args, **kwargs )

        self._event_notifier.raise_event( "default_before", *args, **kwargs )

    def default_process( self, *args: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> None:
        super().default_process( *args, **kwargs )

        self._event_notifier.raise_event( "default_process", *args, **kwargs )

    def default_after( self, *args: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> None:
        super().default_after( *args, **kwargs )

        self._event_notifier.raise_event( "default_after", *args, **kwargs )

    def before_document_start( self ) -> None:
        super().before_document_start()

        self._event_notifier.raise_event( "before_document_start" )

    def process_document_start( self ) -> None:
        super().process_document_start()

        self._event_notifier.raise_event( "process_document_start" )

    def after_document_start( self ) -> None:
        super().after_document_start()

        self._event_notifier.raise_event( "after_document_start" )

    def before_document_end( self ) -> None:
        super().before_document_end()

        self._event_notifier.raise_event( "before_document_end" )

    def process_document_end( self ) -> None:
        super().process_document_end()

        self._event_notifier.raise_event( "process_document_end" )

    def after_document_end( self ) -> None:
        super().after_document_end()

        self._event_notifier.raise_event( "after_document_end" )

    def before_object_start( self ) -> None:
        super().before_object_start()

        self._event_notifier.raise_event( "before_object_start" )

    def process_object_start( self ) -> None:
        super().process_object_start()

        self._event_notifier.raise_event( "process_object_start" )

    def after_object_start( self ) -> None:
        super().after_object_start()

        self._event_notifier.raise_event( "after_object_start" )

    def before_object_end( self ) -> None:
        super().before_object_end()

        self._event_notifier.raise_event( "before_object_end" )

    def process_object_end( self ) -> None:
        super().process_object_end()

        self._event_notifier.raise_event( "process_object_end" )

    def after_object_end( self ) -> None:
        super().after_object_end()

        self._event_notifier.raise_event( "after_object_end" )

    def before_list_start( self ) -> None:
        super().before_list_start()

        self._event_notifier.raise_event( "before_list_start" )

    def process_list_start( self ) -> None:
        super().process_list_start()

        self._event_notifier.raise_event( "process_list_start" )

    def after_list_start( self ) -> None:
        super().after_list_start()

        self._event_notifier.raise_event( "after_list_start" )

    def before_list_end( self ) -> None:
        super().before_list_end()

        self._event_notifier.raise_event( "before_list_end" )

    def process_list_end( self ) -> None:
        super().process_list_end()

        self._event_notifier.raise_event( "process_list_end" )

    def after_list_end( self ) -> None:
        super().after_list_end()

        self._event_notifier.raise_event( "after_list_end" )

    def before_list_item_start( self ) -> None:
        super().before_list_item_start()

        self._event_notifier.raise_event( "before_list_item_start" )

    def process_list_item_start( self ) -> None:
        super().process_list_item_start()

        self._event_notifier.raise_event( "process_list_item_start" )

    def after_list_item_start( self ) -> None:
        super().after_list_item_start()

        self._event_notifier.raise_event( "after_list_item_start" )

    def before_list_item_end( self ) -> None:
        super().before_list_item_end()

        self._event_notifier.raise_event( "before_list_item_end" )

    def process_list_item_end( self ) -> None:
        super().process_list_item_end()

        self._event_notifier.raise_event( "process_list_item_end" )

    def after_list_item_end( self ) -> None:
        super().after_list_item_end()

        self._event_notifier.raise_event( "after_list_item_end" )

    def before_list_item_value_start( self ) -> None:
        super().before_list_item_value_start()

        self._event_notifier.raise_event( "before_list_item_value_start" )

    def process_list_item_value_start( self ) -> None:
        super().process_list_item_value_start()

        self._event_notifier.raise_event( "process_list_item_value_start" )

    def after_list_item_value_start( self ) -> None:
        super().after_list_item_value_start()

        self._event_notifier.raise_event( "after_list_item_value_start" )

    def before_list_item_value_end( self ) -> None:
        super().before_list_item_value_end()

        self._event_notifier.raise_event( "before_list_item_value_end" )

    def process_list_item_value_end( self ) -> None:
        super().process_list_item_value_end()

        self._event_notifier.raise_event( "process_list_item_value_end" )

    def after_list_item_value_end( self ) -> None:
        super().after_list_item_value_end()

        self._event_notifier.raise_event( "after_list_item_value_end" )

    def before_member_start( self ) -> None:
        super().before_member_start()

        self._event_notifier.raise_event( "before_member_start" )

    def process_member_start( self ) -> None:
        super().process_member_start()

        self._event_notifier.raise_event( "process_member_start" )

    def after_member_start( self ) -> None:
        super().after_member_start()

        self._event_notifier.raise_event( "after_member_start" )

    def before_member_end( self ) -> None:
        super().before_member_end()

        self._event_notifier.raise_event( "before_member_end" )

    def process_member_end( self ) -> None:
        super().process_member_end()

        self._event_notifier.raise_event( "process_member_end" )

    def after_member_end( self ) -> None:
        super().after_member_end()

        self._event_notifier.raise_event( "after_member_end" )

    def before_member_key( self, name: str ) -> None:
        super().before_member_key( name )

        self._event_notifier.raise_event( "before_member_key", name )

    def process_member_key( self, name: str ) -> None:
        super().process_member_key( name )

        self._event_notifier.raise_event( "process_member_key", name )

    def after_member_key( self, name: str ) -> None:
        super().after_member_key( name )

        self._event_notifier.raise_event( "after_member_key", name )

    def before_member_value_start( self ) -> None:
        super().before_member_value_start()

        self._event_notifier.raise_event( "before_member_value_start" )

    def process_member_value_start( self ) -> None:
        super().process_member_value_start()

        self._event_notifier.raise_event( "process_member_value_start" )

    def after_member_value_start( self ) -> None:
        super().after_member_value_start()

        self._event_notifier.raise_event( "after_member_value_start" )

    def before_member_value_end( self ) -> None:
        super().before_member_value_end()

        self._event_notifier.raise_event( "before_member_value_end" )

    def process_member_value_end( self ) -> None:
        super().process_member_value_end()

        self._event_notifier.raise_event( "process_member_value_end" )

    def after_member_value_end( self ) -> None:
        super().after_member_value_end()

        self._event_notifier.raise_event( "after_member_value_end" )

    def before_value( self, value: Any ) -> None:
        super().before_value( value )

        self._event_notifier.raise_event( "before_value", value )

    def process_value( self, value: Any ) -> None:
        super().process_value( value )

        self._event_notifier.raise_event( "process_value", value )

    def after_value( self, value: Any ) -> None:
        super().after_value( value )

        self._event_notifier.raise_event( "after_value", value )
