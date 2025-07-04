# Bank Withdrawal Simulation using try-except-finally

try:
    balance = float(input("Enter your account balance: ₹"))
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount > balance:
        raise ValueError("Insufficient balance.")
    
    balance -= amount
    print(f"Withdrawal successful! ₹{amount} withdrawn.")

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"Something went wrong: {e}")

finally:
    print(f"Final balance: ₹{balance:.2f}")
