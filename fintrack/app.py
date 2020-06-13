from models import *
from datetime import datetime
from doctest import master
from tkinter import *
import tkinter.messagebox
import datetime
import os
import webbrowser

db.connect()

'''
1. Create Wallet
2. Add Money to Wallet
3. Create Expense
4. Create Debt
5. Delete A Wallet
6. Delete Expense
7. Delete Debt
'''


def create_wallet():
    name = input("Enter Name for the Wallet: ")
    wallet = Wallet(name=name, amount=0, last_transaction=datetime.now())
    wallet.save()
    print("Wallet Created Successfully..\nCurrent Balance: 0")


def check_wallet():
    wallets = Wallet.select()
    if len(wallets) == 0:
        return 0
    else:
        return 1


def list_wallets():
    wallets = Wallet.select()
    print("Select Wallet ID:")
    for wallet in wallets:
        print(wallet.id, wallet.name)

    wallet_id = int(input("-->"))
    return wallet_id


def topup_wallet():
    wallet_id = list_wallets()
    wallet = Wallet.get(Wallet.id == wallet_id)
    amount = int(input("Enter Amount to Add: "))
    wallet.amount += amount
    wallet.save()

    print(f"Current Balance : {wallet.amount}")


def create_expense():
    name = input("Enter Expense Name: ")
    amount = int(input("Enter Expense Amount: "))
    note = input("Add a Note\n---------------------------------------")
    wallet_id = list_wallets()
    wallet = Wallet.get(Wallet.id == wallet_id)
    expense = Expense(name=name, amount=amount, note=note,
                      wallet=wallet, timestamp=datetime.now())
    transaction = Transaction(amount=amount, wallet=wallet,
                              note=name, is_debit=True, timestamp=datetime.now())
    expense.save()
    transaction.save()


def delete_wallet():
    wallet_id = list_wallets()
    wallet = Wallet.get(Wallet.id == wallet_id)
    wallet.delete_instance()


def list_transactions():
    transactions = Transaction.select()
    for transaction in transactions:
        if transaction.is_debit:
            amount = "-₹" + str(transaction.amount)
        else:
            amount = "+₹" + str(transaction.amount)

        print(transaction.note, amount,
              transaction.wallet, transaction.timestamp, sep=" | ")

def create_debt(wallet_id, debt):
    wallet = Wallet.get(Wallet.id == wallet_id)
    amount = int(input("Enter Debt Amount: "))
    person = input("Enter Debt Name: ")
    note = input("Add a Note\n------")
    deadline = input("Enter the Date: ")

    debt.save()

def delete_expense():
    expense_id = list_transactions()
    expense = Expense.get(Expense.id == expense_id)
    expense.delete_instance()


def delete_debt():
    debt_id = list_transactions()
    debt = Debt.get(Debt.id == debt_id) 
    debt.delete_instance()
          
