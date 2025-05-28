#have a bank account
#a Savings account and Current account

#deposit, withdraw, display balance, display account type

class BankAccount:
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
            
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")
        
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
        
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Applied interest: {interest}. New balance is {self.balance}.")
        
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        
    #overriding the withdraw method to allow overdraft   
    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
            
# Example usage
savings1 = SavingsAccount("SA123", 1000, 5)
savings1.display_balance()
savings1.deposit(200)
savings1.apply_interest()
savings1.withdraw(150)
savings1.display_balance()
print("\n")

current1 = CurrentAccount("CA123", 500, 200)
current1.display_balance()
current1.deposit(300)
current1.withdraw(700)
current1.display_balance()
current1.withdraw(1000)  # This should succeed due to overdraft limit
current1.display_balance()
        