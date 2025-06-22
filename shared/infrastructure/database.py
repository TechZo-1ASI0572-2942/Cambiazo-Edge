from peewee import SqliteDatabase

# Inicializa la base de datos
db = SqliteDatabase('cambiazo.db')

def init_db():
    """Initialize the database and create necessary tables."""
    from lockers.infrastructure.models import Locker  # ← Importación diferida
    db.connect()
    db.create_tables([Locker])
    db.close()
