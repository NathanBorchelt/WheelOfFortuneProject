#Nathan Borchelt
#10 min
from random import choice

class SpinWheel():
    def __init__(self,wheel):
        self.wheel = wheel
    def spin(self):
        spin = choice(self.wheel)

        return spin
    def delMillion(self):
        for item in self.wheel:
            if item == 1_000_000:
                item = 'Bankrupt'