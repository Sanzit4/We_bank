from account import Account

class SavingsAccount :
    limit = 1000 #Limit for savings account


    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount, limit):
        if amount < limit :
            super().withdraw(amount)

