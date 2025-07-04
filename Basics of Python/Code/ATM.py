"""Design a class ATM:
Private balance
Method Withdraw (if sufficient balance)
Method to deposit
Method to check balance
  Use proper validation inside deposit and withdraw methods."""
class ATM:
    def __init__(self,balance):
        self.__balance = balance
    def withdraw(self,sufficient_balance):
        if sufficient_balance > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= sufficient_balance
            print(f"Withdrawal successful. New balance: {self.__balance}")
    def deposit(self,sufficient_balance):
        if sufficient_balance <= 0:
            print("Deposit amount must be positive.")
        else:
            self.__balance += sufficient_balance
            print(f"Deposit successful. New balance: {self.__balance}")
    def check_balance(self):
        print(f"Current balance: {self.__balance}")
# Example usage
atm = ATM(1000)
atm.check_balance()  # Check initial balance
atm.withdraw(200)    # Withdraw 200
atm.check_balance()  # Check balance after withdrawal
atm.deposit(500)     # Deposit 500
atm.check_balance()  # Check balance after deposit
atm.withdraw(1500)   # Attempt to withdraw more than balance
atm.deposit(-100)    # Attempt to deposit a negative amount
atm.check_balance()  # Final balance check