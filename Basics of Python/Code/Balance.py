#Create a class Account with a constructor that initializes balance. 
# Inherit a class Savingsn Account that uses super() to call the parent constructor and adds interest_rate.
#  Print all attributes.
class Account:
    def __init__(self,balance):
        self.balance = balance
        def display_balance(self):
            print(f"Balance: {self.balance}")
class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def display_details(self):
        print(f"Balance: {self.balance}, Interest Rate: {self.interest_rate}")  
savings_account = SavingsAccount(1000, 0.05)
savings_account.display_details() 
