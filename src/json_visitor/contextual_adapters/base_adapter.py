__version__ = r"2.0.0"

from typing import Any, Iterable, Tuple

from ..simple_adapters.scope_adapter import ScopeAdapter
from ..scoping.root_scope import RootScope
from ..scoping.object_scope import ObjectScope
from ..scoping.member_scope import MemberScope
from ..scoping.list_scope import ListScope
from ..scoping.list_item_scope import ListItemScope

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

        scope = self.root_scope

        self.before_document( scope, scope.get_value() )
        self.process_document( scope, scope.get_value() )
        self.after_document( scope, scope.get_value() )

    def after_object_end( self ) -> None:
        """
        Callback invoked after processing the end of an object.
        """

        scope = self.current_scope

        super().after_object_end()

        self.before_object( scope, scope.get_value() )
        self.process_object( scope, scope.get_value() )
        self.after_object( scope, scope.get_value() )

    def after_member_end( self ) -> None:
        """
        Callback invoked after processing the end of a member.
        """

        scope = self.current_scope

        super().after_member_end()

        self.before_member( scope, scope.name_scope.name, scope.value_scope.get_value() )
        self.process_member( scope, scope.name_scope.name, scope.value_scope.get_value() )
        self.after_member( scope, scope.name_scope.name, scope.value_scope.get_value() )

    def after_list_end( self ) -> None:
        """
        Callback invoked after processing the end of a list.
        """

        scope = self.current_scope

        super().after_list_end()

        self.before_list( scope, scope.get_value() )
        self.process_list( scope, scope.get_value() )
        self.after_list( scope, scope.get_value() )

    def after_list_item_end( self ) -> None:
        """
        Callback invoked after processing the end of a list item.
        """

        scope = self.current_scope

        super().after_list_item_end()

        self.before_list_item( scope, scope.item_index, scope.item_value_scope.get_value() )
        self.process_list_item( scope, scope.item_index, scope.item_value_scope.get_value() )
        self.after_list_item( scope, scope.item_index, scope.item_value_scope.get_value() )

    def before_document( self, scope: RootScope, value: Any ) -> None:
        """
        Callback invoked before processing the document.

        Parameters:
            `scope`: the root scope for the document.
            `value`: the value of the document.
        """

        self.default_before( scope, value )

    def process_document( self, scope: RootScope, value: Any ) -> None:
        """
        Callback invoked when processing the document.

        Parameters:
            `root_scope`: the root scope for the document.
        """

        self.default_process( scope, value )

    def after_document( self, scope: RootScope, value: Any ) -> None:
        """
        Callback invoked after processing the document.

        Parameters:
            `root_scope`: the root scope for the document.
        """

        self.default_after( scope, value )

    def before_object( self, scope: ObjectScope, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Callback invoked before processing an object.
        
        Parameters:
            `scope`: the scope for the object.
            `members`: Iterable of tuples of string and value containing the object member data.
        """

        self.default_process( scope, members )

    def process_object( self, scope: ObjectScope, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Callback invoked when processing an object.
        
        Parameters:
            `scope`: the scope for the object.
            `members`: Iterable of tuples of string and value containing the object member data.
        """

        self.default_process( scope, members )

    def after_object( self, scope: ObjectScope, members: Iterable[ Tuple[ str, Any ] ] ) -> None:
        """
        Callback invoked after processing an object.
        
        Parameters:
            `scope`: the scope for the object.
            `members`: Iterable of tuples of string and value containing the object member data.
        """

        self.default_process( scope, members )

    def before_member( self, scope: MemberScope, name: str, value: Any ) -> None:
        """
        Callback invoked before processing an object member.

        Parameters:
            `scope`: the scope for the member.
            `name`: name of the member.
            `value`: value of the member.
        """

        self.default_process( scope, name, value )

    def process_member( self, scope: MemberScope, name: str, value: Any ) -> None:
        """
        Callback invoked when processing an object member.

        Parameters:
            `scope`: the scope for the member.
            `name`: name of the member.
            `value`: value of the member.
        """

        self.default_process( scope, name, value )

    def after_member( self, scope: MemberScope, name: str, value: Any ) -> None:
        """
        Callback invoked after processing an object member.

        Parameters:
            `scope`: the scope for the member.
            `name`: name of the member.
            `value`: value of the member.
        """

        self.default_process( scope, name, value )

    def before_list( self, scope: ListScope, items: Iterable[ Any ] ) -> None:
        """
        Callback invoked before processing a list.
        
        Parameters:
            `scope`: the scope for the list.
            `items`: Iterable of the list items.
        """

        self.default_process( scope, items )

    def process_list( self, scope: ListScope, items: Iterable[ Any ] ) -> None:
        """
        Callback invoked when processing a list.
        
        Parameters:
            `scope`: the scope for the list.
            `items`: Iterable of the list items.
        """

        self.default_process( scope, items )

    def after_list( self, scope: ListScope, items: Iterable[ Any ] ) -> None:
        """
        Callback invoked after processing a list.
        
        Parameters:
            `scope`: the scope for the list.
            `items`: Iterable of the list items.
        """

        self.default_process( scope, items )

    def before_list_item( self, scope: ListItemScope, index_: int, value: Any ) -> None:
        """
        Callback invoked before processing a list item.
        
        Parameters:
            `scope`: the scope for the list item.
            `index_`: list index of the list item.
            `value`: value of the item item.
        """

        self.default_process( scope, index_, value )

    def process_list_item( self, scope: ListItemScope, index_: int, value: Any ) -> None:
        """
        Callback invoked when processing a list item.
        
        Parameters:
            `scope`: the scope for the list item.
            `index_`: list index of the list item.
            `value`: value of the item item.
        """

        self.default_process( scope, index_, value )

    def after_list_item( self, scope: ListItemScope, index_: int, value: Any ) -> None:
        """
        Callback invoked after processing a list item.
        
        Parameters:
            `scope`: the scope for the list item.
            `index_`: list index of the list item.
            `value`: value of the item item.
        """

        self.default_process( scope, index_, value )
