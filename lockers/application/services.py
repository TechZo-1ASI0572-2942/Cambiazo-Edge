"""Application services for the Locker-bounded context."""
import requests
from lockers.domain.entities import Locker
from lockers.domain.services import LockerRecordService
from lockers.infrastructure.repositories import LockerRepository
from lockers.domain.enums.stateEnum import StateEnum


class LockerApplicationService:
    """Application service for managing locker exchange records."""

    def __init__(self):
        """Initialize the LockerApplicationService."""
        self.locker_repository = LockerRepository()
        self.locker_service = LockerRecordService()
        self.external_api_url = "https://cambiazo-backend-bjdkd7hhgqa8gygw.westus-01.azurewebsites.net/api/v2/exchange-lockers"

    def create_locker_record(
        self,
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
        """Create and persist a locker record.

        Args:
            locker_id (str): Locker identifier.
            exchange_id (int): ID of the exchange.
            user_deposit_id (int): ID of the user expected to deposit.
            user_retrieve_id (int): ID of the user expected to retrieve.
            pin_deposit (str): Deposit PIN code.
            pin_retrieve (str): Retrieve PIN code.
            state_exchange (str): State of the locker in the exchange system (e.g., 'empty', 'full', 'delivered').
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
            state_exchange=state_exchange,
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

        update_locker = self.locker_repository.update(locker_id, kwargs)
        self._sync_with_external_api(update_locker)

        return update_locker

    def _sync_with_external_api(self, locker: Locker):
        """
        Envía los datos del locker a la API externa mediante PUT.
        
        Args:
            locker: Entidad del locker actualizado.
        """
        try:
            # Preparar los datos para enviar
            payload = {
                "exchangeId": locker.exchange_id,
                "lockerId": locker.locker_id,
                "state": locker.state,
                "stateExchange": locker.state_exchange
            }
            print(f"Sincronizando locker {locker.locker_id} con API externa: {payload}")
            
            # Hacer la petición PUT a la API externa
            url = f"{self.external_api_url}/{locker.locker_id}"  # Usar locker.locker_id en lugar de locker.id
            print(f"URL de la API externa: {url}")
            response = requests.put(
                f"{self.external_api_url}/{locker.locker_id}",  # Usar locker.id en lugar de locker.locker_id
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=10  # Timeout de 10 segundos
            )
            
            # Log del resultado (opcional)
            if response.status_code == 200:
                print(f"Locker {locker.locker_id} sincronizado exitosamente con API externa")
            else:
                print(f"Error al sincronizar locker {locker.locker_id}: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            # Manejar errores de conexión sin afectar la operación principal
            print(f"Error de conexión con API externa para locker {locker.locker_id}: {e}")
        except Exception as e:
            print(f"Error inesperado al sincronizar con API externa: {e}")


    def get_locker_record(self, locker_id: str):
        """
        Obtiene un locker a partir de su locker_id.
        
        Args:
            locker_id: Identificador del locker a buscar.
        
        Returns:
            Locker: Locker encontrado.
        """
        return self.locker_repository.get(locker_id)