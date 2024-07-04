import os

FILE_NAME = "accounts.txt"

def get_balance(account_number: str) -> float:
    with open(FILE_NAME, 'r') as file:
        for line in file:
            acc, bal = line.strip().split(',')
            if acc == account_number:
                return float(bal)
    raise ValueError(f"Account {account_number} not found")

def update_account(account_number: str, balance: float):
    accounts = []
    with open(FILE_NAME, 'r') as file:
        for line in file:
            acc, bal = line.strip().split(',')
            if acc == account_number:
                accounts.append(f"{acc},{balance}\n")
            else:
                accounts.append(line)
    
    with open(FILE_NAME, 'w') as file:
        file.writelines(accounts)

def deposit(account_number: str, amount: float):
    current_balance = get_balance(account_number)
    new_balance = current_balance + amount
    update_account(account_number, new_balance)

def withdraw(account_number: str, amount: float):
    current_balance = get_balance(account_number)
    if current_balance >= amount:
        new_balance = current_balance - amount
        update_account(account_number, new_balance)
    else:
        raise ValueError("Insufficient funds")

print(get_balance("1001"))
deposit("1001",5)
print(get_balance("1001"))
withdraw("1001",10)
print(get_balance("1001"))
