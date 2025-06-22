# enum for states
from enum import Enum
class StateEnum(Enum):
    # Enum for the state of a locker
    EMPTY = "EMPTY"
    OCCUPIED = "OCCUPIED"
    RESERVED = "RESERVED"
    MAINTENANCE = "MAINTENANCE"

    def __str__(self):
        return self.value
    