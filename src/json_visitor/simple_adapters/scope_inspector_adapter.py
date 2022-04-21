__version__ = r"1.1.0"

from typing import Any, Dict, Iterable, List, Union, TextIO
from io import TextIOWrapper

import sys
from pathlib import Path
from .scope_adapter import ScopeAdapter

class ScopeInspectionAdapter( ScopeAdapter ):
    def __init__( self, **kwargs: Dict[ str, Any ] ):
        """
        Creates a ScopeInspectionAdapter.
        
        Keyword Arguments:
            `output_targets`: iterable of output targets.
            `open_file_mode`: file mode output targets will be opened with; defaults to write ("w").
            `output_console`: boolean which controls if stdout should be written to; defaults to True, indicating stdout will be written to.
            `output_error`: boolean which controls if stderr should be written to; defaults to False, indicating stderr will not be written to.
        """

        super().__init__()

        output_targets: Iterable[ str, Path, TextIO ] = kwargs.get( "output_targets", None )
        if output_targets is None:
            output_targets = []

        open_file_mode = kwargs.get( "open_file_mode", None )
        if open_file_mode is None:
            open_file_mode: str = "w"

        output_console: bool = bool( kwargs.get( "output_console", True ) )
        output_error: bool = bool( kwargs.get( "output_error", False ) )

        self._output_targets: List[ TextIO ] = []

        if output_console:
            self._output_targets.append( sys.stdout )

        if output_error:
            self._output_targets.append( sys.stderr )

        for target in output_targets:
            if isinstance( target, str ):
                target = Path( target )

            if isinstance( target, Path ):
                target = open( target, open_file_mode )

            if not isinstance( target, ( TextIO, TextIOWrapper ) ):
                raise ValueError( "Invalid scope inspection target: target must be a string, path, or text stream." )
            else:
                self._output_targets.append( target )

    def _output_message( self, message: str ) -> None:
        for target in self._output_targets:
            print( message, file = target )
            target.flush()

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
