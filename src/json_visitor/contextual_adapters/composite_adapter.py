from typing import Any, Iterable, Tuple
from .base_adapter import BaseAdapter
from ..scoping.root_scope import RootScope

class CompositeAdapter( BaseAdapter ):
    """
    Implements an adapter which represents zero or more other adapters which must be children of BaseAdapter.
    """

    def __init__( self, *adapters: Iterable[ BaseAdapter ] ):
        for adapter in adapters:
            if not isinstance( adapter, BaseAdapter ):
                raise ValueError( f"Invalid adapter '{ adapter.__class__.__qualname__ }': it must be a child of { BaseAdapter.__qualname__ }" )

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

    def before_document( self, root_scope: RootScope ) -> None:
        """
        Callback invoked before processing the document.

        Parameters:
            `root_scope`: the root scope for the document.
        """

        for adapter in self._adapters:
            adapter.before_document( root_scope )

    def process_document( self, root_scope: RootScope ) -> None:
        """
        Callback invoked when processing the document.

        Parameters:
            `root_scope`: the root scope for the document.
        """

        for adapter in self._adapters:
            adapter.process_document( root_scope )

    def after_document( self, root_scope: RootScope ) -> None:
        """
        Callback invoked after processing the document.

        Parameters:
            `root_scope`: the root scope for the document.
        """

        for adapter in self._adapters:
            adapter.after_document( root_scope )

    def before_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Callback invoked before processing an object.
        
        Parameters:
            `members`: Iterable of tuples of string and value containing the object member data.
        """

        for adapter in self._adapters:
            adapter.before_object( members )

    def process_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Callback invoked when processing an object.
        
        Parameters:
            `members`: Iterable of tuples of string and value containing the object member data.
        """

        for adapter in self._adapters:
            adapter.process_object( members )

    def after_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Callback invoked after processing an object.
        
        Parameters:
            `members`: Iterable of tuples of string and value containing the object member data.
        """

        for adapter in self._adapters:
            adapter.after_object( members )

    def before_member( self, name: str, value: Any ) -> None:
        """
        Callback invoked before processing an object member.

        Parameters:
            `name`: name of the member.
            `value`: value of the member.
        """

        for adapter in self._adapters:
            adapter.before_member( name, value )

    def process_member( self, name: str, value: Any ) -> None:
        """
        Callback invoked when processing an object member.

        Parameters:
            `name`: name of the member.
            `value`: value of the member.
        """

        for adapter in self._adapters:
            adapter.process_member( name, value )

    def after_member( self, name: str, value: Any ) -> None:
        """
        Callback invoked after processing an object member.

        Parameters:
            `name`: name of the member.
            `value`: value of the member.
        """

        for adapter in self._adapters:
            adapter.after_member( name, value )

    def before_list( self, items: Iterable[ Any ] ) -> None:
        """
        Callback invoked before processing a list.
        
        Parameters:
            `items`: Iterable of the list items.
        """

        for adapter in self._adapters:
            adapter.before_list( items )

    def process_list( self, items: Iterable[ Any ] ) -> None:
        """
        Callback invoked when processing a list.
        
        Parameters:
            `items`: Iterable of the list items.
        """

        for adapter in self._adapters:
            adapter.process_list( items )

    def after_list( self, items: Iterable[ Any ] ) -> None:
        """
        Callback invoked after processing a list.
        
        Parameters:
            `items`: Iterable of the list items.
        """

        for adapter in self._adapters:
            adapter.after_list( items )

    def before_list_item( self, index_: int, value: Any ) -> None:
        """
        Callback invoked before processing a list item.
        
        Parameters:
            `index_`: list index of the list item.
            `value`: value of the item item.
        """

        for adapter in self._adapters:
            adapter.before_list_item( index_, value )

    def process_list_item( self, index_: int, value: Any ) -> None:
        """
        Callback invoked when processing a list item.
        
        Parameters:
            `index_`: list index of the list item.
            `value`: value of the item item.
        """

        for adapter in self._adapters:
            adapter.process_list_item( index_, value )

    def after_list_item( self, index_: int, value: Any ) -> None:
        """
        Callback invoked after processing a list item.
        
        Parameters:
            `index_`: list index of the list item.
            `value`: value of the item item.
        """

        for adapter in self._adapters:
            adapter.after_list_item( index_, value )
