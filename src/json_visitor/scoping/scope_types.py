__version__ = r"1.0.0"

from enum import Enum

class ScopeTypes( Enum ):
    Unknown = 0x0
    Root = 0x1
    Object = 0x2
    Member = 0x4
    MemberName = 0x8
    MemberValue = 0x10
    List = 0x20
    ListItem = 0x40
    ListItemValue = 0x80
    SimpleValue = 0x100
    Value = MemberValue | ListItemValue | SimpleValue
