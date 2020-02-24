#nathan Borchelt 5 hours
from spin import *
from chat import *
from person import *
from time import sleep,time
from random import choice
hello there
def letterCheck(phrase,letter):
    letTimes = 0
    if letter in phrase[1]:
        for i in range(len(phrase[1])):
            if phrase[1][i] is letter:
                phrase[0][i] = letter
                letTimes += 1
        return True, phrase,letTimes
    else:
        return False,phrase,letTimes



vowels = ['A','E','I','O','U']
consonant = []
for i in range(65,91):
    if chr(i) not in vowels:
        consonant.append(chr(i))
#for puzzles, format line so:
#[hint,word]
#BOTH must be strings, no number, only letters
puzzles = [['Trash','Cardi B'],['Country','United States of America'],['Phrase','Phrase that Pays'],['Holiday','Christmas'],['Holiday','Halloween'],['Person','George Washington'],['dQw4w9WgXcQ','Never Gonna Give You Up'],['Social Media','Reddit'],['Video Game','Titanfall'],['Video Game','Minecraft']]

wheelNumbers = [500,500,500,700,700,700,'Bankrupt',1_000_000,'Bankrupt',600,600,600,550,550,550,700,700,700,900,900,900,'Bankrupt','Bankrupt','Bankrupt',650,650,650,'Free Play','Free Play','Free Play',700,700,700, 'Lose A Turn','Lose A Turn','Lose A Turn',800,800,800,500,500,500,650,650,650,700,700,700,900,900,900,'Bankrupt','Bankrupt','Bankrupt',5000,5000,5000,800,800,800,900,900,900,1000,1000,1000,600,600,600,800,800,800]

WheelOfFortune = SpinWheel(wheelNumbers)

c1N = input('Player One, enter your name:\n')
#c1A = input('Player One, enter your age:\n')
#c1L = input('Player One, enter your hometown:\n')

c2N = input('Player Two, enter your name:\n')
#c2A = input('Player Two, enter your age:\n')
#c2L = input('Player Two, enter your hometown:\n')

c3N = input('Player Three, enter your name:\n')
#c3A = input('Player Three, enter your age:\n')
#c3L = input('Player Three, enter your hometown:\n')

player1 = Contestant(c1N)
player2 = Contestant(c2N)
player3 = Contestant(c3N)

playerList = [player1,player2,player3]

PatSajak.intro()

gameOver = False
playingRound = 1
usedPuzzles = []

PatSajak.welcome(player1.rtnName())
sleep(2)
PatSajak.welcome(player2.rtnName())
sleep(2)
PatSajak.welcome(player3.rtnName())
sleep(2)

while not(gameOver):
    puzzleSolve = False
    if player1.rtnMoney() == player2.rtnMoney() == player3.rtnMoney():
        playerSpinning = choice(playerList)
    newRoundPuzzle = choice(puzzles)
    while newRoundPuzzle in usedPuzzles:
        newRoundPuzzle = choice(puzzles)
    usedPuzzles.append(newRoundPuzzle)
    puzzleHint,puzzleAnswer = newRoundPuzzle
    puzzleAnswer = puzzleAnswer.upper()

    blankList = ('_' * len(puzzleAnswer))

    puzzleAnswer,blankList = list(puzzleAnswer),list(blankList)

    checkList = [blankList,puzzleAnswer]

    for let in range(len(checkList[1])):
        if checkList[1][let] == ' ':
            checkList[0][let] = ' '
    
    PatSajak.roundStart(playerSpinning.rtnName(),puzzleHint,playingRound)
    usedVowels = []
    while playingRound == 1:
        usedAllVowels = False
        isInPuzzle = True
        if not playerSpinning.loseTurn(playerSpinning.loseTurn()) and isInPuzzle:
            isInPuzzle = False
            playerSpin = WheelOfFortune.spin()
            if playerSpin == 'Lose A Turn':
                playerSpinning.loseTurn(True)
            elif playerSpin == 'Bankrupt':
                playerSpinning.bankrupt()
            PatSajak.spun(playerSpin,playerSpinning.rtnName())
            sleep(.25)
            startTime = time()
            playerInput = input('Input a single letter:\n')
            playerInput = playerInput.upper()
            if playerSpin != 'Lose A Turn' or 'Bankrupt' or 1_000_000:
                if playerSpin == 'Free Play':
                    if len(usedVowels) != len(vowels):
                        if playerInput not in usedVowels:
                            usedVowels.append(playerInput)
                            isInPuzzle, checkList,num = letterCheck(checkList,playerInput)
                            PatSajak.onBoard(num,playerInput)
                        else:
                            PatSajak.used(playerSpinning.rtnName())
                    else:
                        if not usedAllVowels:
                            usedAllVowels = PatSajak.usedAllVowels()
                        else:
                            PatSajak.allVowelsRmd(playerSpinning.rtnName())
                else:
                    if playerInput in vowels:
                        isInPuzzle,checkList,vowelTimes = letterCheck(checkList,playerInput)
                        playerSpinning.buyVowel(vowelTimes)
                        PatSajak.onBoard(vowelTimes,playerInput)
                    else:
                        isInPuzzle,checkList,consonantTimes = letterCheck(checkList,playerInput)
                        playerSpinning.moneyIn(playerSpin,consonantTimes)
                        PatSajak.onBoard(consonantTimes,playerInput)
            




                            

     
'''hangman Code
def letterCheck(phrase,letter):
    if letter in phrase[1]:
        for i in range(len(phrase[1])):
            if phrase[1][i] is letter:
                phrase[0][i] = letter
        return True
    else:
        return False
usedChar = []
while hangmanState != 0 and ('_' in total[0]):
    validLength = True
    validChar = True
    blankLine = ''
    for i in total[0]:
        blankLine += i
    print(blankLine)
    guess = input('Input a letter')
    print('\n'*40)
    if len(guess) != 1:
        print('Only input one(1) character')
        validLength = False
    try:
        guess.lower()
    except:
        print('Enter one of the 26 letters of the English alphabet.')
        validChar = False
    if guess in usedChar:
        validChar = False
        print('Character already used')
'''
        