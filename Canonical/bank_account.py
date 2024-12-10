class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance > 0 and self.balance >= amount:
            self.balance -= amount
            print(f'{amount} successfully withdrawn. Balance left is {self.balance}')
            return self.account_number
        raise ValueError('Amount greater than current balance')
    

bn = BankAccount(21122, 'Akeem')
print(bn.deposit(1000))
print(bn.withdraw(999))

        