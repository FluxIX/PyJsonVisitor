__version__ = r"1.1.0"

from typing import Any, Dict, Iterable, List

from .scope_types import ScopeTypes
from .scope import Scope
from .value_scope import ValueScope

class SimpleValueScope( ValueScope ):
    """
    Implements a JSON simple value node scope.
    """

    def __init__( self, parent: Scope = None, initial_value: Any = None, is_initial_value: bool = False ):
        super().__init__( ScopeTypes.SimpleValue, parent )


        self.set_value( initial_value, is_initial_value = bool( is_initial_value ) )

    def get_value( self ) -> Any:
        """
        Gets the value of the member node.
        
        Returns:
            The value of the member node.
        """

        return self._value

    def set_value( self, value: Any, **kwargs: Dict[ str, Any ] ) -> None:
        """
        Sets the value of the member node.
        
        Arguments:
            `value`: the value to set the member node to.
            
        Keyword Arguments:
            `is_initial_value`: `True` indicating if the value being set is the initial value, `False` if the value being set is not the initial value.

        Notes:
            - when setting the initial value, the `value` is set but the `has_value` is set to `False`; all other value set operations set the `has_value` to `True`.
        """

        is_initial_value: bool = bool( kwargs.get( "is_initial_value", False ) )

        self._value: Any = value
        self._has_value: bool = not is_initial_value

    value = property( fget = get_value, fset = set_value )

    @property
    def has_value( self ) -> bool:
        """
        Indicates if the scope value has been set.
        
        Returns:
            `True` if the scope value has been set, `False` otherwise.
        """

        return self._has_value

    def clear_value( self ) -> None:
        """
        Clears the scope value.
        """

        self.set_value( None, is_initial_value = False )

    def _get_repr_param_strings( self ) -> List[ str ]:
        parent_str: str = f"parent = { repr( None ) }"
        value_str: str = f"initial_value = { repr( self.get_value() ) }"
        is_initial_value_str: str = f"is_initial_value = { repr( not self.has_value ) }"

        return [ parent_str, value_str, is_initial_value_str ]

    def _get_children_scopes( self ) -> Iterable[ Scope ]:
        return tuple()
