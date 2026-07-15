class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return self.balance


    def withdraw(self, amount):

        if amount > self.balance:
            raise Exception("Insufficient funds")

        self.balance -= amount

        return self.balance