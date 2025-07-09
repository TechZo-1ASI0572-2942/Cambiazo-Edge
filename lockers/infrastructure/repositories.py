"""
Repository for locker record persistence.

Handles saving locker records to the database using Peewee ORM models.
"""
from lockers.domain.entities import Locker as LockerEntity
from lockers.infrastructure.models import Locker as LockerModel


class LockerRepository:
    """
    Repository for managing Locker entity persistence.
    """

    @staticmethod
    def save(locker: LockerEntity) -> LockerEntity:
        """
        Save a Locker entity to the database.

        Args:
            locker (LockerEntity): The locker entity to persist.

        Returns:
            LockerEntity: The saved locker entity with assigned ID.
        """
        record = LockerModel.create(
            locker_id=locker.locker_id,
            exchange_id=locker.exchange_id,
            user_deposit_id=locker.user_deposit_id,
            user_retrieve_id=locker.user_retrieve_id,
            pin_deposit=locker.pin_deposit,
            pin_retrieve=locker.pin_retrieve,
            state_exchange=locker.state_exchange,
            state=locker.state,
            last_synced=locker.last_synced
        )
        return LockerEntity(
            locker_id=record.locker_id,
            exchange_id=record.exchange_id,
            user_deposit_id=record.user_deposit_id,
            user_retrieve_id=record.user_retrieve_id,
            pin_deposit=record.pin_deposit,
            pin_retrieve=record.pin_retrieve,
            state_exchange=record.state_exchange,
            state=record.state,
            last_synced=record.last_synced,
            id=record.id
        )

    @staticmethod
    def update(locker_id: str, data: dict):
        """
        Actualiza el Locker identificado por locker_id con los datos suministrados.

        Args:
            locker_id (str): Identificador del locker a actualizar.
            data (dict): Diccionario con los campos a actualizar.

        Returns:
            LockerEntity: Entidad actualizada del locker.
        """
        query = LockerModel.update(**data).where(LockerModel.locker_id == locker_id)
        rows_modified = query.execute()
        if rows_modified == 0:
            raise ValueError("Locker not found")
        updated_record = LockerModel.get(LockerModel.locker_id == locker_id)
        # Retorna una instancia de la entidad Locker con los datos actualizados.
        return LockerEntity(
            locker_id=updated_record.locker_id,
            exchange_id=updated_record.exchange_id,
            user_deposit_id=updated_record.user_deposit_id,
            user_retrieve_id=updated_record.user_retrieve_id,
            pin_deposit=updated_record.pin_deposit,
            pin_retrieve=updated_record.pin_retrieve,
            state_exchange=updated_record.state_exchange,
            state=updated_record.state,
            last_synced=updated_record.last_synced
        )
    
    @staticmethod
    def get(locker_id: str):
        """
        Obtiene el Locker identificado por locker_id.
        
        Args:
            locker_id (str): Identificador del locker a obtener.
        
        Returns:
            LockerEntity: Entidad del locker encontrado.
        """
        updated_record = LockerModel.get_or_none(LockerModel.locker_id == locker_id)
        if updated_record is None:
            raise ValueError("Locker not found")
        return LockerEntity(
            locker_id=updated_record.locker_id,
            exchange_id=updated_record.exchange_id,
            user_deposit_id=updated_record.user_deposit_id,
            user_retrieve_id=updated_record.user_retrieve_id,
            pin_deposit=updated_record.pin_deposit,
            pin_retrieve=updated_record.pin_retrieve,
            state_exchange=updated_record.state_exchange,
            state=updated_record.state,
            last_synced=updated_record.last_synced
        )