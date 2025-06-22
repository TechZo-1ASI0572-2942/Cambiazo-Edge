"""Interface services for the Locker-bounded context."""

from flask import Blueprint, request, jsonify
from lockers.application.services import LockerApplicationService
from lockers.domain.stateEnum import StateEnum
from datetime import datetime

locker_api = Blueprint("locker_api", __name__)

# Initialize application service
locker_service = LockerApplicationService()


@locker_api.route("/records", methods=["POST"])
def create_locker_record():
    """Handle POST requests to create a locker record.

    Expects JSON with locker_id, exchange_id, user_deposit_id, user_retrieve_id,
    pin_deposit, pin_retrieve, and optional state / last_synced.

    Returns:
        tuple: (JSON response, status code).
    """
    data = request.json

    try:
        locker = locker_service.create_locker_record(
            locker_id=data["locker_id"],
            exchange_id=data["exchange_id"],
            user_deposit_id=data["user_deposit_id"],
            user_retrieve_id=data["user_retrieve_id"],
            pin_deposit=data["pin_deposit"],
            pin_retrieve=data["pin_retrieve"],
            state=data.get("state", StateEnum.EMPTY.value),
            last_synced=data.get("last_synced")
        )

        return jsonify({
            "id": locker.id,
            "locker_id": locker.locker_id,
            "exchange_id": locker.exchange_id,
            "user_deposit_id": locker.user_deposit_id,
            "user_retrieve_id": locker.user_retrieve_id,
            "pin_deposit": locker.pin_deposit,
            "pin_retrieve": locker.pin_retrieve,
            "state": locker.state,
            "last_synced": locker.last_synced.isoformat() if locker.last_synced else None
        }), 201

    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@locker_api.route("/records/<locker_id>", methods=["PUT"])
def update_locker_record(locker_id):
    """Endpoint para actualizar los datos del locker identificado por locker_id."""
    if not locker_id:
        return jsonify({"error": "Locker ID is required"}), 400
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    if not locker_id.isalnum():
        return jsonify({"error": "Locker ID must be alphanumeric"}), 400
    
    data = request.json
    data['last_synced'] = datetime.now().isoformat() if 'last_synced' not in data else data['last_synced']
    try:
        updated_locker = locker_service.update_locker_record(locker_id, **data)
        return jsonify({
            "locker_id": updated_locker.locker_id,
            "exchange_id": updated_locker.exchange_id,
            "user_deposit_id": updated_locker.user_deposit_id,
            "user_retrieve_id": updated_locker.user_retrieve_id,
            "pin_deposit": updated_locker.pin_deposit,
            "pin_retrieve": updated_locker.pin_retrieve,
            "state": updated_locker.state,
            "last_synced": updated_locker.last_synced
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@locker_api.route("/records/<locker_id>", methods=["GET"])
def get_locker_record(locker_id):
    """Endpoint para obtener los datos de un locker por su locker_id."""
    try:
        locker = locker_service.get_locker_record(locker_id)
        # Seria segura para last_synced: si tiene isoformat se usa, sino se devuelve el mismo valor
        if hasattr(locker.last_synced, "isoformat"):
            last_synced = locker.last_synced.isoformat()
        else:
            last_synced = locker.last_synced
        return jsonify({
            "locker_id": locker.locker_id,
            "exchange_id": locker.exchange_id,
            "user_deposit_id": locker.user_deposit_id,
            "user_retrieve_id": locker.user_retrieve_id,
            "pin_deposit": locker.pin_deposit,
            "pin_retrieve": locker.pin_retrieve,
            "state": locker.state,
            "last_synced": last_synced
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404