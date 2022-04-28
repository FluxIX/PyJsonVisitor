__version__ = r"2.0.0"

from typing import Any, Dict, Iterable, List, Tuple, Iterator
from .scope_types import ScopeTypes

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
            if distance > len( lineage ):
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
