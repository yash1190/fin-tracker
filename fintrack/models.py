from peewee import *

db = SqliteDatabase('fintrack.db')


class Wallet(Model):
    name = CharField()
    amount = IntegerField()
    last_transaction = DateTimeField()

    class Meta:
        database = db


class Expense(Model):
    name = CharField()
    amount = IntegerField()
    note = TextField()
    timestamp = DateTimeField()
    wallet = ForeignKeyField(Wallet, backref="expenses")

    class Meta:
        database = db


class Transaction(Model):
    amount = IntegerField()
    timestamp = DateTimeField()
    wallet = ForeignKeyField(Wallet, backref="transactions")
    note = TextField()
    is_debit = BooleanField()

    class Meta:
        database = db


class Debt(Model):
    wallet = ForeignKeyField(Wallet, backref="debts")
    is_lending = BooleanField()
    amount = IntegerField()
    when = DateTimeField()
    deadline = DateTimeField()
    person = CharField()
    note = TextField()
    is_resolved = BooleanField()

    class Meta:
        database = db


if __name__ == "__main__":
    db.connect()
    db.create_tables([Wallet, Expense, Transaction, Debt])
