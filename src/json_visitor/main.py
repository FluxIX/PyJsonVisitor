__version__ = r"1.0.0"

from typing import Any, Dict, Iterable, Union

import os
import sys
from argparse import ArgumentParser, FileType, Namespace
from pathlib import Path
from . import __name__ as PackageName
from .contextual_adapters.composite_adapter import CompositeAdapter
from .contextual_adapters.inspector_adapter import InspectionAdapter
from .subscription.contextual_subscription import ContextualSubscription
from .json_visitor import JsonVisitor

class _ExpandedFileType( FileType ):
    def __init__( self, **kwargs: Dict[ str, Any ] ):
        mode = kwargs.get( "mode", "r" )
        bufsize = kwargs.get( "bufsize", -1 )
        encoding = kwargs.get( "encoding", None )
        errors = kwargs.get( "errors", None )

        super().__init__( mode, bufsize, encoding, errors )

        relative_path = kwargs.get( "relative_path", None )
        if relative_path is None:
            relative_path: str = os.getcwd()
        if isinstance( relative_path, str ):
            relative_path: Path = Path( relative_path )
        self._relative_path: Path = relative_path

    def __call__( self, string ):
        if string != "-" and not os.path.isabs( string ):
            string = self._relative_path.joinpath( string ).resolve( True )

        return super().__call__( string )

    def __repr__( self ):
        # Adapted from: argparse.py's FileType.__repr__ implementation

        args = tuple()
        kwargs = [( 'mode', self._mode ), ( 'bufsize', self._bufsize ), ( 'encoding', self._encoding ), ( 'errors', self._errors ), ( 'relative_path', self._relative_path )]
        args_str = ', '.join( [repr( arg ) for arg in args if arg != -1] +
                             ['%s=%r' % ( kw, arg ) for kw, arg in kwargs
                              if arg is not None] )
        return '%s(%s)' % ( type( self ).__name__, args_str )

def _build_argument_parser( file_relative_path: Union[ Path, str ] = None ):
    parser: ArgumentParser = ArgumentParser( description = "Processes the input JSON strings or files and outputs the visitation events.", prog = PackageName )

    info_parser = parser.add_mutually_exclusive_group( required = False )
    info_parser.add_argument( "-i", "--output-processing-info", dest = "info_enabled", action = "store_true", help = "Enables the output of the processing information. This is the default." )
    info_parser.add_argument( "-I", "--suppress-processing-info", dest = "info_enabled", action = "store_false", help = "Suppresses the output of the processing information." )
    info_parser.set_defaults( info_enabled = True )

    parser.add_argument( "-f", "--file", type = _ExpandedFileType( mode = "r", relative_path = file_relative_path ), dest = "inputs", nargs = 1, action = "extend", help = "JSON file path to process; relative paths are relative to the current working directory.", metavar = "<file path>" )
    parser.add_argument( "-s", "--string", type = str, dest = "inputs", nargs = 1, action = "extend", help = "JSON string literal to process.", metavar = "<string literal>" )

    return parser

def main( args = None ) -> int:
    """
    A JSON visitor driver which will print the scoping events of the strings specified on the strings or files.
    
    Parameters:
        `args`: input parameters to parse. If `None`, parameters are read from `sys.stdin`.
    
    Returns:
        Integer representing the error code.
        0: No error.
        1. No input source provided.
        2. Error processing one or more of the input sources.
    """

    if args is None:
        args = sys.argv[ 1: ]

    arg_parser: ArgumentParser = _build_argument_parser()
    processed_args: Namespace = arg_parser.parse_args( args )
    inputs = processed_args.inputs

    if inputs is None or len( inputs ) == 0:
        print( f"No input provided.", file = sys.stderr )
        error_code = 1
    else:
        for input_ in inputs:
            subscription: ContextualSubscription = ContextualSubscription()

            count: int = 0

            def increment_count( *args: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> None:
                nonlocal count
                count += 1

            subscription.register( "default_process", increment_count )

            adapters = [
                InspectionAdapter(),
                subscription,
            ]

            try:
                JsonVisitor( CompositeAdapter( *adapters ) ).visit( input_ )
            except Exception as e:
                print( f"Error executing commands from '{ input_ }': { e }", file = sys.stderr )
                error_code = 2
            else:
                error_code = 0

            if processed_args.info_enabled:
                print( f"Number of scope events processed: { count }" )

    return error_code
