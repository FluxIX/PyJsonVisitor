__version__ = r"1.0.0"

from typing import Any, Dict, Iterable, List

class Scope( object ):
    """
    Implements a JSON node scope.
    """

    def __init__( self, parent: "Scope" = None ):
        self._parent: Scope = parent

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
