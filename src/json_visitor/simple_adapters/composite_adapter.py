from typing import Any, Iterable, Tuple
from .base_adapter import BaseAdapter

class CompositeAdapter( BaseAdapter ):
    """
    Implements an adapter which represents zero or more other adapters which must be children of BaseAdapter.
    """

    def __init__( self, *adapters: Iterable[ BaseAdapter ] ):
        for adapter in adapters:
            if not isinstance( adapter, BaseAdapter ):
                raise ValueError( f"Invalid adapter '{ adapter.__qualname__ }': it must be a child of { BaseAdapter.__qualname__ }" )

        self._adapters: Tuple[ BaseAdapter ] = tuple( adapters )

    def before_document_start( self ) -> None:
        """
        Callback invoked before processing the start of the document.
        """

        for adapter in self._adapters:
            adapter.before_document_start()

    def process_document_start( self ) -> None:
        """
        Callback invoked when processing the start of the document.
        """

        for adapter in self._adapters:
            adapter.process_document_start()

    def after_document_start( self ) -> None:
        """
        Callback invoked after processing the start of the document.
        """

        for adapter in self._adapters:
            adapter.after_document_start()

    def before_document_end( self ) -> None:
        """
        Callback invoked before processing the end of the document.
        """

        for adapter in self._adapters:
            adapter.before_document_end()

    def process_document_end( self ) -> None:
        """
        Callback invoked when processing the end of the document.
        """

        for adapter in self._adapters:
            adapter.process_document_end()

    def after_document_end( self ) -> None:
        """
        Callback invoked after processing the end of the document.
        """

        for adapter in self._adapters:
            adapter.after_document_end()

    def before_object_start( self ) -> None:
        """
        Callback invoked before processing the start of an object.
        """

        for adapter in self._adapters:
            adapter.before_object_start()

    def process_object_start( self ) -> None:
        """
        Callback invoked when processing the start of an object.
        """

        for adapter in self._adapters:
            adapter.process_object_start()

    def after_object_start( self ) -> None:
        """
        Callback invoked after processing the start of an object.
        """

        for adapter in self._adapters:
            adapter.after_object_start()

    def before_object_end( self ) -> None:
        """
        Callback invoked before processing the end of an object.
        """

        for adapter in self._adapters:
            adapter.before_object_end()

    def process_object_end( self ) -> None:
        """
        Callback invoked when processing the end of an object.
        """

        for adapter in self._adapters:
            adapter.process_object_end()

    def after_object_end( self ) -> None:
        """
        Callback invoked after processing the end of an object.
        """

        for adapter in self._adapters:
            adapter.after_object_end()

    def before_list_start( self ) -> None:
        """
        Callback invoked before processing the start of a list.
        """

        for adapter in self._adapters:
            adapter.before_list_start()

    def process_list_start( self ) -> None:
        """
        Callback invoked when processing the start of a list.
        """

        for adapter in self._adapters:
            adapter.process_list_start()

    def after_list_start( self ) -> None:
        """
        Callback invoked after processing the start of a list.
        """

        for adapter in self._adapters:
            adapter.after_list_start()

    def before_list_end( self ) -> None:
        """
        Callback invoked before processing the end of a list.
        """

        for adapter in self._adapters:
            adapter.before_list_end()

    def process_list_end( self ) -> None:
        """
        Callback invoked when processing the end of a list.
        """

        for adapter in self._adapters:
            adapter.process_list_end()

    def after_list_end( self ) -> None:
        """
        Callback invoked after processing the end of a list.
        """

        for adapter in self._adapters:
            adapter.after_list_end()

    def before_list_item_start( self ) -> None:
        """
        Callback invoked before processing the start of a list item.
        """

        for adapter in self._adapters:
            adapter.before_list_item_start()

    def process_list_item_start( self ) -> None:
        """
        Callback invoked when processing the start of a list item.
        """

        for adapter in self._adapters:
            adapter.process_list_item_start()

    def after_list_item_start( self ) -> None:
        """
        Callback invoked after processing the start of a list item.
        """

        for adapter in self._adapters:
            adapter.after_list_item_start()

    def before_list_item_end( self ) -> None:
        """
        Callback invoked before processing the end of a list item.
        """

        for adapter in self._adapters:
            adapter.before_list_item_end()

    def process_list_item_end( self ) -> None:
        """
        Callback invoked when processing the end of a list item.
        """

        for adapter in self._adapters:
            adapter.process_list_item_end()

    def after_list_item_end( self ) -> None:
        """
        Callback invoked after processing the end of a list item.
        """

        for adapter in self._adapters:
            adapter.after_list_item_end()

    def before_list_item_value_start( self ) -> None:
        """
        Callback invoked before processing the start of a list item value.
        """

        for adapter in self._adapters:
            adapter.before_list_item_value_start()

    def process_list_item_value_start( self ) -> None:
        """
        Callback invoked when processing the start of a list item value.
        """

        for adapter in self._adapters:
            adapter.process_list_item_value_start()

    def after_list_item_value_start( self ) -> None:
        """
        Callback invoked after processing the start of a list item value.
        """

        for adapter in self._adapters:
            adapter.after_list_item_value_start()

    def before_list_item_value_end( self ) -> None:
        """
        Callback invoked before processing the end of a list item value.
        """

        for adapter in self._adapters:
            adapter.before_list_item_value_end()

    def process_list_item_value_end( self ) -> None:
        """
        Callback invoked when processing the end of a list item value.
        """

        for adapter in self._adapters:
            adapter.process_list_item_value_end()

    def after_list_item_value_end( self ) -> None:
        """
        Callback invoked after processing the end of a list item value.
        """

        for adapter in self._adapters:
            adapter.after_list_item_value_end()

    def before_member_start( self ) -> None:
        """
        Callback invoked before processing the start of a member.
        """

        for adapter in self._adapters:
            adapter.before_member_start()

    def process_member_start( self ) -> None:
        """
        Callback invoked when processing the start of a member.
        """

        for adapter in self._adapters:
            adapter.process_member_start()

    def after_member_start( self ) -> None:
        """
        Callback invoked after processing the start of a member.
        """

        for adapter in self._adapters:
            adapter.after_member_start()

    def before_member_end( self ) -> None:
        """
        Callback invoked before processing the end of a member.
        """

        for adapter in self._adapters:
            adapter.before_member_end()

    def process_member_end( self ) -> None:
        """
        Callback invoked when processing the end of a member.
        """

        for adapter in self._adapters:
            adapter.process_member_end()

    def after_member_end( self ) -> None:
        """
        Callback invoked after processing the end of a member.
        """

        for adapter in self._adapters:
            adapter.after_member_end()

    def before_member_key( self, name: str ) -> None:
        """
        Callback invoked before processing the member key.
        
        Parameters:
            `name`: The member key.
        """

        for adapter in self._adapters:
            adapter.before_member_key( name )

    def process_member_key( self, name: str ) -> None:
        """
        Callback invoked when processing the member key.
        
        Parameters:
            `name`: The member key.
        """

        for adapter in self._adapters:
            adapter.process_member_key( name )

    def after_member_key( self, name: str ) -> None:
        """
        Callback invoked after processing the member key.
        
        Parameters:
            `name`: The member key.
        """

        for adapter in self._adapters:
            adapter.after_member_key( name )

    def before_member_value_start( self ) -> None:
        """
        Callback invoked before processing the start of a member value.
        """

        for adapter in self._adapters:
            adapter.before_member_value_start()

    def process_member_value_start( self ) -> None:
        """
        Callback invoked when processing the start of a member value.
        """

        for adapter in self._adapters:
            adapter.process_member_value_start()

    def after_member_value_start( self ) -> None:
        """
        Callback invoked after processing the start of a member value.
        """

        for adapter in self._adapters:
            adapter.after_member_value_start()

    def before_member_value_end( self ) -> None:
        """
        Callback invoked before processing the end of a member value.
        """

        for adapter in self._adapters:
            adapter.before_member_value_end()

    def process_member_value_end( self ) -> None:
        """
        Callback invoked when processing the end of a member value.
        """

        for adapter in self._adapters:
            adapter.process_member_value_end()

    def after_member_value_end( self ) -> None:
        """
        Callback invoked after processing the end of a member value.
        """

        for adapter in self._adapters:
            adapter.after_member_value_end()

    def before_value( self, value: Any ) -> None:
        """
        Callback invoked before processing the value.

        Parameters:
            `value`: the value being processed.
        """

        for adapter in self._adapters:
            adapter.before_value( value )

    def process_value( self, value: Any ) -> None:
        """
        Callback invoked when processing the value.

        Parameters:
            `value`: the value being processed.
        """

        for adapter in self._adapters:
            adapter.process_value( value )

    def after_value( self, value: Any ) -> None:
        """
        Callback invoked after processing the value.

        Parameters:
            `value`: the value being processed.
        """

        for adapter in self._adapters:
            adapter.after_value( value )
