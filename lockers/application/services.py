"""Application services for the Locker-bounded context."""

from lockers.domain.entities import Locker
from lockers.domain.services import LockerRecordService
from lockers.infrastructure.repositories import LockerRepository
from lockers.domain.stateEnum import StateEnum


class LockerApplicationService:
    """Application service for managing locker exchange records."""

    def __init__(self):
        """Initialize the LockerApplicationService."""
        self.locker_repository = LockerRepository()
        self.locker_service = LockerRecordService()

    def create_locker_record(
        self,
        locker_id: str,
        exchange_id: int,
        user_deposit_id: int,
        user_retrieve_id: int,
        pin_deposit: str,
        pin_retrieve: str,
        state: str = StateEnum.EMPTY,
        last_synced: str | None = None
    ) -> Locker:
        """Create and persist a locker record.

        Args:
            locker_id (str): Locker identifier.
            exchange_id (int): ID of the exchange.
            user_deposit_id (int): ID of the user expected to deposit.
            user_retrieve_id (int): ID of the user expected to retrieve.
            pin_deposit (str): Deposit PIN code.
            pin_retrieve (str): Retrieve PIN code.
            state (str): Initial state. Defaults to "waiting_deposit".
            last_synced (str | None): Optional last sync timestamp.

        Returns:
            Locker: The created locker domain entity.

        Raises:
            ValueError: If input data is invalid.
        """
        locker = self.locker_service.create_record(
            locker_id=locker_id,
            exchange_id=exchange_id,
            user_deposit_id=user_deposit_id,
            user_retrieve_id=user_retrieve_id,
            pin_deposit=pin_deposit,
            pin_retrieve=pin_retrieve,
            state=state,
            last_synced=last_synced
        )

        return self.locker_repository.save(locker)

    def update_locker_record(self, locker_id: str, **kwargs):
        """
        Actualiza un locker a partir de locker_id con los datos proporcionados en kwargs.

        Args:
            locker_id: Identificador del locker a actualizar.
            **kwargs: Campos a modificar.

        Returns:
            Locker: Locker actualizado.
        """
        return self.locker_repository.update(locker_id, kwargs)

    def get_locker_record(self, locker_id: str):
        """
        Obtiene un locker a partir de su locker_id.
        
        Args:
            locker_id: Identificador del locker a buscar.
        
        Returns:
            Locker: Locker encontrado.
        """
        return self.locker_repository.get(locker_id)