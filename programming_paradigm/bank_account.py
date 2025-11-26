class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")