"""
Peewee ORM model for locker records.

Defines the Locker database table structure for storing locker exchange data locally on the IoT Edge.
"""
from peewee import (
    Model, AutoField, CharField, IntegerField, DateTimeField
)

from shared.infrastructure.database import db


class Locker(Model):
    """
    ORM model for the lockers table.
    Represents a locker exchange entry in the IoT Edge database.
    """
    id = AutoField()
    locker_id = CharField()
    exchange_id = IntegerField()
    user_deposit_id = IntegerField()
    user_retrieve_id = IntegerField()
    pin_deposit = CharField()
    pin_retrieve = CharField()
    state = CharField()
    last_synced = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'lockers'
