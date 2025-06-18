from account import Account

class CurrentAccount (Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    currentAccount =  CurrentAccount(1000)
    currentAccount.deposite(300)
    print(currentAccount.balance)