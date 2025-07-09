# enum for states
from enum import Enum
class StateExchangeEnum(Enum):
    # Enum for the state of exchange lockers
    EMPTY = "EMPTY"
    FULL = "FULL"
    DELIVERED = "DELIVERED"

    def __str__(self):
        return self.value