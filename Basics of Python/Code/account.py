#Create a class Account with a private attribute __balance. Create:
#A getter method get_balance()
#A setter method set_balance() that ensures balance cannot be negative
# Create an object, try to access balance directly, then use methods instead.
class Account:
    def __init__(self, balance, amount=0):
        self.__balance = balance  
        self._amount = amount

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance < 0:
            print("Balance cannot be negative.")
        else:
            self.__balance = balance
account = Account(1000)
try:
    print("Direct access to balance:", account.__balance)
except AttributeError:
    print("AttributeError: Cannot access private attribute __balance directly.")
print("Balance using getter:", account.get_balance())
account.set_balance(1500)
print("Balance after update using setter:", account.get_balance())
account.set_balance(-500)
print("Balance after trying to set negative value:", account.get_balance())