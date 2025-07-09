# Este script envía peticiones POST a la API para crear lockers vacíos.
import requests

url = "http://127.0.0.1:5000/api/v1/lockers/records"

# Número de lockers a crear
numero_lockers = 100

for i in range(51, numero_lockers + 1):
    locker_id = f"A{i:02d}"  # Formato: A01, A02, etc.
    data = {
        "locker_id": locker_id,
        "exchange_id": 0,
        "user_deposit_id": 0,
        "user_retrieve_id": 0,
        "pin_deposit": "0000",  # En lugar de "", se asigna un PIN por defecto
        "pin_retrieve": "0000", # En lugar de "", se asigna un PIN por defecto
        "state_exchange": "EMPTY",  # Estado inicial del locker en el sistema de intercambio
        "state": "AVAILABLE"
        # "last_synced" se omite, quedando en null
    }
    response = requests.post(url, json=data)
    print(f"Locker {locker_id} - Código: {response.status_code}, Respuesta: {response.json()}")