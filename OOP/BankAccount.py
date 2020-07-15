# this is simple program for bank account


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdrawal(self, amount):
        if self.balance < amount:
            print("Cannot overdraw from the account")
            return

        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit this amount")
            return

        self.balance = self.balance + amount
        return self.balance

    def __str__(self):
        return "Current Balance of User : " + self.owner + " is : " + str(self.balance)


accnt1 = BankAccount("Bala", 10000)

accnt2 = BankAccount("Kumaran", 3000)

accnt1.deposit(3000)
accnt2.deposit(6000)

print(accnt1)
print(accnt2)

accnt1.withdrawal(2000000)
print(accnt1)

accnt2.withdrawal(2000)
print(accnt2)
