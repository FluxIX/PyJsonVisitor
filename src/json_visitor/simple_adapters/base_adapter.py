from typing import Any, Dict, Iterable

class BaseAdapter( object ):
    """
    Implements a base adapter to inherit from for JSON visitation.

    This adapter does not track scope to implement low-level callbacks.
    """

    def default_before( self, *args: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> None:
        """
        Default callback invoked when before processing a node.
        """

        pass

    def default_process( self, *args: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> None:
        """
        Default callback invoked when processing a node.
        """

        pass

    def default_after( self, *args: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> None:
        """
        Default callback invoked when after processing a node.
        """

        pass

    def before_document_start( self ) -> None:
        """
        Callback invoked before processing the start of the document.
        """

        self.default_before()

    def process_document_start( self ) -> None:
        """
        Callback invoked when processing the start of the document.
        """

        self.default_process()

    def after_document_start( self ) -> None:
        """
        Callback invoked after processing the start of the document.
        """

        self.default_after()

    def before_document_end( self ) -> None:
        """
        Callback invoked before processing the end of the document.
        """

        self.default_before()

    def process_document_end( self ) -> None:
        """
        Callback invoked when processing the end of the document.
        """

        self.default_process()

    def after_document_end( self ) -> None:
        """
        Callback invoked after processing the end of the document.
        """

        self.default_after()

    def before_object_start( self ) -> None:
        """
        Callback invoked before processing the start of an object.
        """

        self.default_before()

    def process_object_start( self ) -> None:
        """
        Callback invoked when processing the start of an object.
        """

        self.default_process()

    def after_object_start( self ) -> None:
        """
        Callback invoked after processing the start of an object.
        """

        self.default_after()

    def before_object_end( self ) -> None:
        """
        Callback invoked before processing the end of an object.
        """

        self.default_before()

    def process_object_end( self ) -> None:
        """
        Callback invoked when processing the end of an object.
        """

        self.default_process()

    def after_object_end( self ) -> None:
        """
        Callback invoked after processing the end of an object.
        """

        self.default_after()

    def before_list_start( self ) -> None:
        """
        Callback invoked before processing the start of a list.
        """

        self.default_before()

    def process_list_start( self ) -> None:
        """
        Callback invoked when processing the start of a list.
        """

        self.default_process()

    def after_list_start( self ) -> None:
        """
        Callback invoked after processing the start of a list.
        """

        self.default_after()

    def before_list_end( self ) -> None:
        """
        Callback invoked before processing the end of a list.
        """

        self.default_before()

    def process_list_end( self ) -> None:
        """
        Callback invoked when processing the end of a list.
        """

        self.default_process()

    def after_list_end( self ) -> None:
        """
        Callback invoked after processing the end of a list.
        """

        self.default_after()

    def before_list_item_start( self ) -> None:
        """
        Callback invoked before processing the start of a list item.
        """

        self.default_before()

    def process_list_item_start( self ) -> None:
        """
        Callback invoked when processing the start of a list item.
        """

        self.default_process()

    def after_list_item_start( self ) -> None:
        """
        Callback invoked after processing the start of a list item.
        """

        self.default_after()

    def before_list_item_end( self ) -> None:
        """
        Callback invoked before processing the end of a list item.
        """

        self.default_before()

    def process_list_item_end( self ) -> None:
        """
        Callback invoked when processing the end of a list item.
        """

        self.default_process()

    def after_list_item_end( self ) -> None:
        """
        Callback invoked after processing the end of a list item.
        """

        self.default_after()

    def before_list_item_value_start( self ) -> None:
        """
        Callback invoked before processing the start of a list item value.
        """

        self.default_before()

    def process_list_item_value_start( self ) -> None:
        """
        Callback invoked when processing the start of a list item value.
        """

        self.default_process()

    def after_list_item_value_start( self ) -> None:
        """
        Callback invoked after processing the start of a list item value.
        """

        self.default_after()

    def before_list_item_value_end( self ) -> None:
        """
        Callback invoked before processing the end of a list item value.
        """

        self.default_before()

    def process_list_item_value_end( self ) -> None:
        """
        Callback invoked when processing the end of a list item value.
        """

        self.default_process()

    def after_list_item_value_end( self ) -> None:
        """
        Callback invoked after processing the end of a list item value.
        """

        self.default_after()

    def before_member_start( self ) -> None:
        """
        Callback invoked before processing the start of a member.
        """

        self.default_before()

    def process_member_start( self ) -> None:
        """
        Callback invoked when processing the start of a member.
        """

        self.default_process()

    def after_member_start( self ) -> None:
        """
        Callback invoked after processing the start of a member.
        """

        self.default_after()

    def before_member_end( self ) -> None:
        """
        Callback invoked before processing the end of a member.
        """

        self.default_before()

    def process_member_end( self ) -> None:
        """
        Callback invoked when processing the end of a member.
        """

        self.default_process()

    def after_member_end( self ) -> None:
        """
        Callback invoked after processing the end of a member.
        """

        self.default_after()

    def before_member_key( self, name: str ) -> None:
        """
        Callback invoked before processing the member key.
        
        Parameters:
            `name`: The member key.
        """

        self.default_before( name )

    def process_member_key( self, name: str ) -> None:
        """
        Callback invoked when processing the member key.
        
        Parameters:
            `name`: The member key.
        """

        self.default_process( name )

    def after_member_key( self, name: str ) -> None:
        """
        Callback invoked after processing the member key.
        
        Parameters:
            `name`: The member key.
        """

        self.default_after( name )

    def before_member_value_start( self ) -> None:
        """
        Callback invoked before processing the start of a member value.
        """

        self.default_before()

    def process_member_value_start( self ) -> None:
        """
        Callback invoked when processing the start of a member value.
        """

        self.default_process()

    def after_member_value_start( self ) -> None:
        """
        Callback invoked after processing the start of a member value.
        """

        self.default_after()

    def before_member_value_end( self ) -> None:
        """
        Callback invoked before processing the end of a member value.
        """

        self.default_before()

    def process_member_value_end( self ) -> None:
        """
        Callback invoked when processing the end of a member value.
        """

        self.default_process()

    def after_member_value_end( self ) -> None:
        """
        Callback invoked after processing the end of a member value.
        """

        self.default_after()

    def before_value( self, value: Any ) -> None:
        """
        Callback invoked before processing the value.

        Parameters:
            `value`: the value being processed.
        """

        self.default_before( value )

    def process_value( self, value: Any ) -> None:
        """
        Callback invoked when processing the value.

        Parameters:
            `value`: the value being processed.
        """

        self.default_process( value )

    def after_value( self, value: Any ) -> None:
        """
        Callback invoked after processing the value.

        Parameters:
            `value`: the value being processed.
        """

        self.default_after( value )
