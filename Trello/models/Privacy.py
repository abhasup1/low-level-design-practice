from enum import Enum,auto
from exceptions.TypeException import TypeException

class Privacy(Enum):
    PUBLIC=auto()
    PRIVATE=auto()

    @staticmethod
    def type(val):
        if val.upper()=="PUBLIC":
            return Privacy.PUBLIC
        elif val.upper()=="PRIVATE":
            return Privacy.PRIVATE
        else:
            raise TypeException(val)

