class BankAccount:
    def __init__(self,account_holder,balance):
        self.__account_holder=account_holder
        self.__balance=balance
    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def account_type(self):
        return "Bank Account"
class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings Account"
class CurrentAccount(BankAccount):
    def account_type(self):#overriding the method from the parent class
        return "Current Account"
    #
def print_account_type(account):
    print(f"Account Holder: {account.get_account_holder()}, Account Type: {account.account_type()}, Balance: {account.get_balance()}")
savings_account = SavingsAccount("Alice", 1500)
current_account = CurrentAccount("Bob", 2500)   
accounts = [savings_account, current_account]
for account in accounts:
    print_account_type(account)
