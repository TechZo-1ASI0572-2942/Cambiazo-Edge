"""Domain services for the Locker-bounded context."""

from datetime import datetime, timezone
from dateutil.parser import parse
from lockers.domain.enums.stateEnum import StateEnum

from lockers.domain.entities import Locker


class LockerRecordService:
    """Service for managing locker records in the IoT Edge."""

    def __init__(self):
        """Initialize the LockerRecordService."""
        pass

    @staticmethod
    def create_record(
        locker_id: str,
        exchange_id: int,
        user_deposit_id: int,
        user_retrieve_id: int,
        pin_deposit: str,
        pin_retrieve: str,
        state_exchange: str,
        state: str = StateEnum.AVAILABLE,
        last_synced: str | None = None
    ) -> Locker:
        """Create a new locker record.

        Args:
            locker_id (str): Physical locker ID.
            exchange_id (int): Exchange ID from backend.
            user_deposit_id (int): ID of the deposit user.
            user_retrieve_id (int): ID of the retrieve user.
            pin_deposit (str): PIN for deposit access.
            pin_retrieve (str): PIN for retrieve access.
            state_exchange (str): State of the locker in the exchange system (e.g., 'empty', 'full', 'delivered').
            state (str): Initial state of the locker.
            last_synced (str | None): Last sync timestamp (ISO 8601).

        Returns:
            Locker: The constructed Locker domain entity.

        Raises:
            ValueError: If input data is invalid or incorrectly formatted.
        """
        try:
            # Validations
            if not (pin_deposit and pin_retrieve):
                raise ValueError("PINs must be provided")

            parsed_last_synced = (
                parse(last_synced).astimezone(timezone.utc)
                if last_synced else None
            )

        except Exception as e:
            raise ValueError(f"Invalid input format: {e}")

        return Locker(
            locker_id=locker_id,
            exchange_id=exchange_id,
            user_deposit_id=user_deposit_id,
            user_retrieve_id=user_retrieve_id,
            pin_deposit=pin_deposit,
            pin_retrieve=pin_retrieve,
            state_exchange=state_exchange,
            state=state,
            last_synced=parsed_last_synced
        )
