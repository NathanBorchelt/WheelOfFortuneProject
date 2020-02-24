#nathan Borchelt
#1 hour
import datetime
date = datetime.datetime.today()

class PatSajak():
    @staticmethod
    def intro():
        print("It's America's game, Wheeeeeeeeeeeeeel of Fortune! The world's most popular gameshow! And now, from the Sony Studios, here they are the stars of our show, Pat Sajak and Vanna White")
    @staticmethod
    def welcome(name):
        print("Pat Sajak: \"I am here with " + name+ '\"')
    @staticmethod
    def roundStart(player,hint, playingRound):
        print('Pat Sajak: "As we enter Round '+str(playingRound)+', '+player+' is spinning first. The hint is '+hint+'."')
    @staticmethod
    def spun(value,name):
        if value == 'Bankrupt':
            print("Pat Sajak: \"Oh, I'm so sorry, but we got to take it all from you.\"")
        elif value == 1_000_000:
            print("Pat Sajak: \"Wow, " + name + ", you sure got lucky, $1,000,000 is up for grabs. All you have todo is solve.\"")
        elif value == 'Lose A Turn':
            print("Pat Sajak: \"Oh, so sorry to see that happen, but hey atleast it is not bankruptcy\"")
        elif value == 'Free Play':
            print("Pat Sajak: \"Hey, look at that, you landed on the free play. There are no penalties for wrong answers and vowels are free. What do you want to do?\"")
        else:
            print("Pat Sajak: \""+name+", you landed on the $"+str(value)+" What do you want to do?\"")
    @staticmethod
    def finalGame(value,name,million):
        print('Pat Sajak: "Well, you made it to the final round. ', name+'. You','do'if million else "don't",'have the million. Best of luck on your spin, but first, I need 3 constanents and a vowel."')
    @staticmethod
    def invalidInput(name):
        print('Pat Sajak: "I am sorry, '+name+', that is not a valid answer, try again next round."')
    @staticmethod
    def sorry(name):
        print('Pat Sajak: "I am sorry, '+name+', that is on the board."')
    @staticmethod
    def used(name):
        print('Pat Sajak: "I am sorry, '+name+', that has already been used."')
    @staticmethod
    def allVowelsRmd(name):
        print('Pat Sajak: "I am sorry, '+name+', but all the vowels have been used."')
    @staticmethod
    def usedAllVowels():
        print('Pat Sajak: "Okay folks, we are out of vowels"')
        return True
    @staticmethod
    def onBoard(times, letter):
        if times != 0:
            print('Pat Sajak: "',str(times),letter,'s' if times > 1 else '','"')
        else:
            print('Pat Sajak: "I am sorry, that is not on the board."')


    





