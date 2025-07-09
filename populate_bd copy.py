# Este script envía peticiones POST a la API para crear lockers vacíos.
import requests

url = "http://localhost:8080/api/v2/lockers"

# Número de lockers a crear
numero_lockers = 100
API_KEY = "eyJhbGciOiJIUzM4NCJ9.eyJzdWIiOiJqb3NlcGhwcnVlYmExMjNAZ21haWwuY29tIiwiaWF0IjoxNzUyMDM2NTM5LCJleHAiOjE3NTI2NDEzMzl9.CUAyEigF7oFzRpy6MMXHvg43W1LL1ij3wPA65mx-h7zUPHxAuVlEB-B9TPC1dTq2"


for i in range(81, numero_lockers + 1):
    locker_id = f"A{i:02d}"  # Formato: A01, A02, etc.
    data = {
        "lockerId": locker_id,
        "lockerState": "AVAILABLE",
        "locationId": 5
    }
    response = requests.post(url, json=data, headers={"Content-Type": "application/json", "Authorization": "Bearer "+ API_KEY})
    print(f"Locker {locker_id} - Código: {response.status_code}, Respuesta: {response.json()}")