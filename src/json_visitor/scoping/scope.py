__version__ = r"2.1.0"

from typing import Any, Dict, Iterable, List, Tuple, Iterator
from .scope_types import ScopeTypes
from ..tokenizer.token_processor import TokenProcessor
from ..tokenizer.scope_walker import ScopeWalker

class Scope( object ):
    """
    Implements a JSON node scope.
    """

    def __init__( self, scope_type: ScopeTypes, parent: "Scope" = None ):
        self._type: ScopeTypes = scope_type
        self._parent: Scope = parent

    @property
    def type( self ) -> ScopeTypes:
        return self._type

    def get_parent( self ) -> "Scope":
        """
        Gets the parent of the current scope.
        
        Returns:
        The parent of the current scope; if the current scope has no parent scope, `None` is returned instead.
        """

        return self._parent

    def set_parent( self, value: "Scope" ) -> None:
        """
        Sets the parent of the current scope to the given value.
        """

        self._parent = value

    parent = property( fget = get_parent, fset = set_parent )

    @property
    def has_parent( self ) -> bool:
        """
        Indicates if the current scope has a parent scope.
        
        Returns:
        `True` if the current scope has a parent, `False` otherwise.
        """

        return self.parent is not None

    @property
    def is_root( self ) -> bool:
        """
        Indicates if the current scope is the root scope.
        
        Returns:
        `True` if the current scope is the root scope, `False` otherwise.
        """

        return not self.has_parent

    def get_value( self ) -> Any:
        """
        Gets the evaluated value of the current scope.
        """

        raise NotImplementedError( "Child must implement." )

    def set_value( self, value: Any, **kwargs: Dict[ str, Any ] ) -> None:
        """
        Sets the evaluated value of the current scope.
        """

        raise NotImplementedError( "Child must implement." )

    def _get_scope_tree( self, value: Any, **kwargs: Dict[ str, Any ] ) -> "Scope":
        from ..simple_adapters.scope_adapter import ScopeAdapter

        scope_adapter: ScopeAdapter = ScopeAdapter()
        processor: TokenProcessor = TokenProcessor( ScopeWalker( scope_adapter ) )
        processor.process_json( value )

        result: "Scope" = scope_adapter.root_scope.child_scope

        return result

    def _get_repr_param_strings( self ) -> List[ str ]:
        return [ f"parent = { repr( self.parent ) }" ]

    def __repr__( self, *args: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> str:
        return self._get_representation_string( *self._get_repr_param_strings() )

    def _get_str_param_strings( self ) -> List[ str ]:
        return []

    def __str__( self, *args: Iterable[ Any ], **kwargs: Dict[ str, Any ] ) -> str:
        return self._get_representation_string( *self._get_str_param_strings() )

    def _get_representation_string( self, *component_strings: Iterable[ str ] ) -> str:
        if len( component_strings ) > 0:
            parameter_str: str = f" { ', '.join( component_strings ) } "
        else:
            parameter_str: str = ""

        return f"{ self.__class__.__qualname__ }({ parameter_str })"

    def _walk_lineage( self ) -> None:
        yield self
        scope = self
        while scope.has_parent:
            scope = scope.parent
            yield scope

    def get_lineage( self, root_first: bool = True ) -> Iterator[ "Scope" ]:
        """
        Gets the lineage of the current scope. If the given `root_first` is True, the root of the scope chain of the current scope is the first element and the current scope is the last element, otherwise the current scope is first element and the root scope is the last element.
        
        Returns:
            Iterator of the scope chain in the specified order.
        """

        result: Iterator[ "Scope" ] = self._walk_lineage()
        if root_first:
            result = reversed( tuple( result ) )

        return result

    @property
    def lineage( self ) -> Iterator[ "Scope" ]:
        """
        Gets the lineage of the current scope from root of the scope chain to the current scope; the root appears as the first element and the current scope appears last.

        Returns:
            Iterator of the scope chain from root to current scope.
        """

        return self.get_lineage( root_first = True )

    @property
    def depth( self ) -> int:
        """
        Gets the depth of the current scope in the scope chain; if the current scope is the root of the chain, the depth is zero.

        Returns:
            Integer value representing the depth of the current scope in the scope chain.
        """

        return len( tuple( self.get_lineage( root_first = False ) ) ) - 1

    def get_ancestor( self, distance: int = 1 ) -> "Scope":
        """
        Gets the ancestor of the current scope which is the given distance away from the current scope.

        Returns:
            The ancestor of the current scope which is the given distance away from the current scope.
        """

        if distance < 0:
            result: "Scope" = None
        else:
            lineage: Tuple[ "Scope" ] = tuple( self.get_lineage( root_first = False ) )
            if distance > ( len( lineage ) - 1 ):
                result: "Scope" = None
            else:
                result: "Scope" = lineage[ distance ]

        return result

    def has_ancestor( self, distance = 1 ) -> bool:
        """
        Indicates of the current scope has an ancestor which is the given distance away from the current scope.
        
        Returns:
            `True` if the current scope has an ancestor which is the given distance away from the current scope, `False` otherwise.
        """

        return self.get_ancestor( distance ) is not None

    def _get_children_scopes( self ) -> Iterable[ "Scope" ]:
        """
        Gets the immediate children scopes of the current scope.

        Returns:
            The immediate children scopes of the current scope.
        """

        raise NotImplementedError( "Child must implement." )

    def _get_descendant_scopes( self, min_depth: int, max_depth: int = None ) -> Iterable[ "Scope" ]:
        """
        Gets the descendant scopes for the current scopes which have a depth of at least the given minimum and, if the given maximum depth is not None, a depth of at most the given maximum depth.

        Arguments:
            `min_depth`: the minimum depth of descendant scopes to select.
            `max_depth`: if `None`, no maximum depth is specified, otherwise the maximum depth of descendant scopes to select.

        Returns:
            The descendant scopes which match the given minimum and maximum depths.
        """

        if not isinstance( min_depth, int ):
            raise ValueError( f"Minimum depth ({ min_depth }) must be an integer." )
        elif max_depth is not None and not isinstance( max_depth, int ):
            raise ValueError( f"Maximum depth ({ max_depth }) must be either an integer or None." )
        elif min_depth <= 0:
            raise ValueError( f"Minimum depth ({ min_depth }) must be a positive integer." )
        elif max_depth is not None and max_depth <= 0:
            raise ValueError( f"Maximum depth ({ max_depth }) must be either a positive integer or None." )
        elif max_depth is None or min_depth <= max_depth:
            current_depth: int = 1
            current_ply = tuple( self._get_children_scopes() )
            while ( max_depth is None or current_depth <= max_depth ) and len( current_ply ) > 0:
                new_ply = []

                for scope in current_ply:
                    if current_depth >= min_depth:
                        yield scope
                    new_ply.extend( scope._get_children_scopes() )

                current_depth += 1
                current_ply = new_ply

    def find_children_scopes( self, **kwargs: Dict[ str, Any ] ) -> Iterable[ "Scope" ]:
        """
        Finds the children scopes of the current scope which match the given criteria.

        Returns:
            The children scopes of the current scope which match the given criteria.
        """

        keyword_args = kwargs.copy()
        keyword_args.update( min_depth = 1, max_depth = 1 )
        return self.find_descendant_scopes( **keyword_args )

    def find_descendant_scopes( self, **kwargs: Dict[ str, Any ] ) -> Iterable[ "Scope" ]:
        """
        Finds the descendant scopes of the current scope which match the given criteria.

        Keyword Arguments:
            `min_depth`: minimum depth to select descendants. If specified, the minimum depth must be positive.
            `max_depth`: maximum depth to select descendants. If specified, the maximum depth must be positive; if `None` or not specified, there is no maximum depth.
            `filter`: expression used to filter the select the descendants. If `None` or not specified, all descendants are selected.

        Returns:
            The children scopes of the current scope which match the given criteria.
        """

        min_depth: int = int( kwargs.get( "min_depth", 1 ) )
        max_depth = kwargs.get( "max_depth", None )
        if max_depth is not None:
            max_depth: int = int( max_depth )

        result = tuple( self._get_descendant_scopes( min_depth, max_depth ) )

        filter_ = kwargs.get( "filter", None )
        if filter_ is not None:
            result = filter( filter_, result )

        return result

    def replace_children_scope_values( self, value: Any, **kwargs: Dict[ str, Any ] ) -> None:
        """
        Replaces value of the children scopes specified by the given keyword arguments with the given value if a matching child scope is found.
        
        Arguments:
            `value` new evaluated value for the located children.
        """

        keyword_args = kwargs.copy()
        keyword_args.update( min_depth = 1, max_depth = 1 )
        return self.replace_descendant_scope_values( value, **keyword_args )

    def replace_descendant_scope_values( self, value: Any, **kwargs: Dict[ str, Any ] ) -> None:
        """
        Replaces value of the descendant scopes specified by the given keyword arguments with the given value if a matching child scope is found.
        
        Arguments:
            `value` new evaluated value for the located children.

        Keyword Arguments:
            `min_depth`: minimum depth to select descendants. If specified, the minimum depth must be positive.
            `max_depth`: maximum depth to select descendants. If specified, the maximum depth must be positive; if `None` or not specified, there is no maximum depth.
            `filter`: expression used to filter the select the descendants. If `None` or not specified, all descendants are selected.
        """

        for descendant_scope in self.find_descendant_scopes( **kwargs ):
            if descendant_scope is not None:
                descendant_scope.set_value( value )
