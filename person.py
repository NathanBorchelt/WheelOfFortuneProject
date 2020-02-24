#30 min nathan borchelt
class Contestant:
    def __init__(self,name='PlaceHolder', money = 0, million = False,loseATurn = False):
        self.name = name

        self.money = money
        self.million = million
        self.loseATurn = loseATurn
    def rtnName(self):
        return(self.name)
    def rtnAge(self):
        return (str(self.age))
    def rtnLocation(self):
        return self.location
    def rtnMoney(self):
        return self.money
    def getMil(self):
        self.million = True
    def bankrupt(self):
        self.money = 0
        self.million = False
    def moneyIn(self,letVal,numLets):
        for i in range(numLets):
            self.money += letVal
        print('New Total: $'+str(self.money))
    def buyVowel(self,numVwl):
        for i in range(numVwl):
            self.money -= 250
        print('New Total: $'+str(self.money))
    def loseTurn(self,lose=False):
        if lose:
            self.loseATurn = not self.loseATurn
        return self.loseATurn

    

