"""Domain entities for the Locker-bounded context."""

from datetime import datetime
from lockers.domain.enums.stateEnum import StateEnum

class Locker:
    """Represents a locker exchange record in the Locker context.

    Attributes:
        id (int, optional): Unique identifier for the locker record.
        locker_id (str): Identifier of the physical locker.
        exchange_id (int): Exchange identifier from the main system.
        user_deposit_id (int): User who is expected to deposit an item.
        user_retrieve_id (int): User who is expected to retrieve the item.
        pin_deposit (str): PIN code required for deposit.
        pin_retrieve (str): PIN code required for retrieval.
        state (str): Current state of the locker: 'available', 'in use' and 'out of service'.
        state_exchange (str, optional): State of the locker in the exchange system (e.g., 'empty', 'full', 'delivered').
        last_synced (datetime, optional): Last synchronization timestamp with main system.
    """

    def __init__(
        self,
        locker_id: str,
        exchange_id: int,
        user_deposit_id: int,
        user_retrieve_id: int,
        pin_deposit: str,
        pin_retrieve: str,
        state_exchange: str,
        state: str = StateEnum.AVAILABLE,
        last_synced: datetime|None = None,
        id: int = None,
    ):
        """Initialize a Locker instance.

        Args:
            locker_id (str): Physical locker ID.
            exchange_id (int): Related exchange ID.
            user_deposit_id (int): ID of user who deposits the item.
            user_retrieve_id (int): ID of user who retrieves the item.
            pin_deposit (str): PIN for deposit access.
            pin_retrieve (str): PIN for retrieve access.
            state (str): Current state of the locker: 'available', 'in use' and 'out of service'.
            state_exchange (str, optional): State of the locker in the exchange system (e.g., 'empty', 'full', 'delivered').
            last_synced (datetime, optional): Timestamp of last sync. Defaults to None.
            id (int, optional): Unique identifier. Defaults to None.
        """
        self.id = id
        self.locker_id = locker_id
        self.exchange_id = exchange_id
        self.user_deposit_id = user_deposit_id
        self.user_retrieve_id = user_retrieve_id
        self.pin_deposit = pin_deposit
        self.pin_retrieve = pin_retrieve
        self.state = state
        self.state_exchange = state_exchange
        self.last_synced = last_synced
