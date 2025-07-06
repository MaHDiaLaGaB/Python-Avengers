
class BankAccount:
    bank_name = "Global Bank"
    accounts = []

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount
        print(f"the {amount} has been deposited to ur account")

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
    
ac_1 = BankAccount("mohamed", 2000.0)
ac_2 = BankAccount("sanad", 4500.0)
ac_3 = BankAccount("anam")

# ac_1.deposit(3.0)
# print(ac_1.balance)

ac_2.transfer(ac_3, 500)

print(ac_3.balance)