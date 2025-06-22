from flask import Flask
from lockers.interfaces.services import locker_api
from shared.infrastructure.database import init_db

app = Flask(__name__)
app.register_blueprint(locker_api, url_prefix="/api/v1/lockers")  # <- Prefijo opcional pero útil

first_request = True

@app.before_request
def setup():
    global first_request
    if first_request:
        first_request = False
        init_db()

if __name__ == "__main__":
    app.run(debug=True)
