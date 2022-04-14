__version__ = r"1.0.0"

from typing import Any, Iterable, Tuple

from ..simple_adapters.scope_adapter import ScopeAdapter
from ..scoping.root_scope import RootScope

class BaseAdapter( ScopeAdapter ):
    """
    Implements a base adapter to inherit from for JSON visitation.

    This adapter tracks scope and stores data to implement higher-level callbacks.
    """

    def __init__( self ):
        super().__init__()
        self._persistent_data = True

    def after_document_end( self ) -> None:
        """
        Callback invoked after processing the end of the document.
        """

        super().after_document_end()

        self.before_document( self.root_scope )
        self.process_document( self.root_scope )
        self.after_document( self.root_scope )

    def after_object_end( self ) -> None:
        """
        Callback invoked after processing the end of an object.
        """

        scope = self.current_scope

        super().after_object_end()

        self.before_object( scope.get_value() )
        self.process_object( scope.get_value() )
        self.after_object( scope.get_value() )

    def after_member_end( self ) -> None:
        """
        Callback invoked after processing the end of a member.
        """

        scope = self.current_scope

        super().after_member_end()

        self.before_member( scope.name_scope.name, scope.value_scope.get_value() )
        self.process_member( scope.name_scope.name, scope.value_scope.get_value() )
        self.after_member( scope.name_scope.name, scope.value_scope.get_value() )

    def after_list_end( self ) -> None:
        """
        Callback invoked after processing the end of a list.
        """

        scope = self.current_scope

        super().after_list_end()

        self.before_list( scope.get_value() )
        self.process_list( scope.get_value() )
        self.after_list( scope.get_value() )

    def after_list_item_end( self ) -> None:
        """
        Callback invoked after processing the end of a list item.
        """

        scope = self.current_scope

        super().after_list_item_end()

        self.before_list_item( scope.item_index, scope.item_value_scope.get_value() )
        self.process_list_item( scope.item_index, scope.item_value_scope.get_value() )
        self.after_list_item( scope.item_index, scope.item_value_scope.get_value() )

    def before_document( self, root_scope: RootScope ) -> None:
        """
        Callback invoked before processing the document.

        Parameters:
            `root_scope`: the root scope for the document.
        """

        self.default_before( root_scope )

    def process_document( self, root_scope: RootScope ) -> None:
        """
        Callback invoked when processing the document.

        Parameters:
            `root_scope`: the root scope for the document.
        """

        self.default_process( root_scope )

    def after_document( self, root_scope: RootScope ) -> None:
        """
        Callback invoked after processing the document.

        Parameters:
            `root_scope`: the root scope for the document.
        """

        self.default_after( root_scope )

    def before_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Callback invoked before processing an object.
        
        Parameters:
            `members`: Iterable of tuples of string and value containing the object member data.
        """

        self.default_process( members )

    def process_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Callback invoked when processing an object.
        
        Parameters:
            `members`: Iterable of tuples of string and value containing the object member data.
        """

        self.default_process( members )

    def after_object( self, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Callback invoked after processing an object.
        
        Parameters:
            `members`: Iterable of tuples of string and value containing the object member data.
        """

        self.default_process( members )

    def before_member( self, name: str, value: Any ) -> None:
        """
        Callback invoked before processing an object member.

        Parameters:
            `name`: name of the member.
            `value`: value of the member.
        """

        self.default_process( name, value )

    def process_member( self, name: str, value: Any ) -> None:
        """
        Callback invoked when processing an object member.

        Parameters:
            `name`: name of the member.
            `value`: value of the member.
        """

        self.default_process( name, value )

    def after_member( self, name: str, value: Any ) -> None:
        """
        Callback invoked after processing an object member.

        Parameters:
            `name`: name of the member.
            `value`: value of the member.
        """

        self.default_process( name, value )

    def before_list( self, items: Iterable[ Any ] ) -> None:
        """
        Callback invoked before processing a list.
        
        Parameters:
            `items`: Iterable of the list items.
        """

        self.default_process( items )

    def process_list( self, items: Iterable[ Any ] ) -> None:
        """
        Callback invoked when processing a list.
        
        Parameters:
            `items`: Iterable of the list items.
        """

        self.default_process( items )

    def after_list( self, items: Iterable[ Any ] ) -> None:
        """
        Callback invoked after processing a list.
        
        Parameters:
            `items`: Iterable of the list items.
        """

        self.default_process( items )

    def before_list_item( self, index_: int, value: Any ) -> None:
        """
        Callback invoked before processing a list item.
        
        Parameters:
            `index_`: list index of the list item.
            `value`: value of the item item.
        """

        self.default_process( index_, value )

    def process_list_item( self, index_: int, value: Any ) -> None:
        """
        Callback invoked when processing a list item.
        
        Parameters:
            `index_`: list index of the list item.
            `value`: value of the item item.
        """

        self.default_process( index_, value )

    def after_list_item( self, index_: int, value: Any ) -> None:
        """
        Callback invoked after processing a list item.
        
        Parameters:
            `index_`: list index of the list item.
            `value`: value of the item item.
        """

        self.default_process( index_, value )
