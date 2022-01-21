class Player:
    playerNum = 0
    accountBalance = 0
    income = 0

    def __init__(self, playerNum, income):
        self.playerNum = playerNum
        self.income = income

    def getBalance(self):
        return round(self.accountBalance,2)

    def addBalance(self, amount):
        self.accountBalance = self.accountBalance + amount

    def subtractBalance(self, amount):
        self.accountBalance = self.accountBalance - amount

    def addIncome(self):
        self.accountBalance = self.accountBalance + self.income
