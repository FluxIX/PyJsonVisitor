from typing import Any, Iterable
from .scope_adapter import ScopeAdapter

class ScopeInspectionAdapter( ScopeAdapter ):
    def __init__( self ):
        super().__init__()

        self._output_message = lambda message: print( message )

    def _print_message( self, name, *values: Iterable[ Any ] ) -> None:
        if len( values ) > 0:
            message = f'{ name }: { ", ".join( [ f"({ index_ }: { value })" for index_, value in enumerate( values ) ] ) }'
        else:
            message = f"{ name }"

        self._output_message( message )

    def process_document_start( self ) -> None:
        super().process_document_start()

        self._print_message( 'document_start', )

    def process_document_end( self ) -> None:
        super().process_document_end()

        self._print_message( 'document_end', )

    def process_object_start( self ) -> None:
        super().process_object_start()

        self._print_message( 'object_start', )

    def process_object_end( self ) -> None:
        super().process_object_end()

        self._print_message( 'object_end', )

    def process_list_start( self ) -> None:
        super().process_list_start()

        self._print_message( 'list_start', )

    def process_list_end( self ) -> None:
        super().process_list_end()

        self._print_message( 'list_end', )

    def process_list_item_start( self ) -> None:
        super().process_list_item_start()

        self._print_message( 'list_item_start', )

    def process_list_item_end( self ) -> None:
        super().process_list_item_end()

        self._print_message( 'list_item_end', )

    def process_list_item_value_start( self ) -> None:
        super().process_list_item_value_start()

        self._print_message( 'list_item_value_start', )

    def process_list_item_value_end( self ) -> None:
        super().process_list_item_value_end()

        self._print_message( 'list_item_value_end', )

    def process_member_start( self ) -> None:
        super().process_member_start()

        self._print_message( 'member_start', )

    def process_member_end( self ) -> None:
        super().process_member_end()

        self._print_message( 'member_end', )

    def process_member_key( self, name: str ) -> None:
        super().process_member_key( name )

        self._print_message( 'member_key', name )

    def process_member_value_start( self ) -> None:
        super().process_list_item_value_start()

        self._print_message( 'member_value_start', )

    def process_member_value_end( self ) -> None:
        super().process_member_end()

        self._print_message( 'member_value_end', )

    def process_value( self, value: Any ) -> None:
        super().process_value( value )

        self._print_message( 'value', value )
