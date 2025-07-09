# enum for states
from enum import Enum
class StateEnum(Enum):
    # Enum for the state of a locker
    AVAILABLE = "AVAILABLE"
    IN_USE = "IN_USE"
    OUT_OF_SERVICE = "OUT_OF_SERVICE"
    
    def __str__(self):
        return self.value
    