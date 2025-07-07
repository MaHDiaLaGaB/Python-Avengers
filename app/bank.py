import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="my_app.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
    )

class DepositError(Exception):
    """Deposit error the value is maybe in (-)"""
    def __init__(self, message="Deposit error the value is maybe in (-)"):
        super().__init__(message)


class BankAccount:
    bank_name = "Global Bank"
    accounts = []

    def __init__(self, owner: str, balance: float = 0.0):
        logging.info("bank is open")
        self.owner = owner
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount: float):
        if amount <= 0:
            logging.error("no money")
            raise DepositError(message="no enough money")
        self.balance += amount
        logging.info(f"the {amount} has been deposited to ur account")
        

    def withdraw(self, amount: float):
        if amount >= self.balance:
            raise ValueError("Insufficient balance")
        
        self.balance -= amount
        print(f"you withdraw {amount} from {self.owner}'s account")
    
    def transfer(self, to_account, amount: float):
        if not isinstance(to_account, BankAccount):
            raise TypeError("no bank account found")
        if amount > self.balance:
            raise ValueError(" no balance")
        self.balance -= amount
        to_account.balance += amount
        print(f"{amount} has been transfered to the account {to_account.owner}")
    
    def __str__(self):
        return f"Account Owner: {self.owner}\nBalance is {self.balance}"
    
    def __repr__(self):
        return "hello i am reper"
try:
    print("creating account")
    ac_1 = BankAccount("mohamed", 2000.0)
    ac_2 = BankAccount("sanad", 4500.0)
    ac_3 = BankAccount("anam")
    ac_4 = "any account"

    print("try to deposit (-) amount")
    ac_1.deposit(50)
    print(ac_1)

    print("try to withdraw on red")
    ac_2.withdraw(500)

    print("transfer more than we have")
    ac_1.transfer(ac_2, 2000)
    print(ac_2)

except DepositError as de:
    print("it's value error", de)

except TypeError as te:
    print("it's type error", te)

except Exception as e:
    print("it's general error")

else:
    print("all banck op has been done")

finally:
    print("final account states")
    BankAccount.accounts