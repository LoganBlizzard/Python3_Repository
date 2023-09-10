#First personal project attempt 9/7/23
#Dice roller

import sys
import random


def getRandomRolls(amountOfRolls, dieNumber):
    rolls = []
    highestDieNumber = 0
    if dieNumber == 1:
        highestDieNumber = 3
    elif dieNumber == 2:
        highestDieNumber = 6
    elif dieNumber == 3:
        highestDieNumber = 10
    elif dieNumber == 4:
        highestDieNumber = 20
    
    for i in range(amountOfRolls):
        roll = random.randint(1, highestDieNumber)
        rolls.append(roll)
    return rolls


print("Welcome to Dice Roller!")

while True:

    print("What kind of die would you like to roll?")
    desiredDice = ''
    while desiredDice not in "1 2 3 4".split():
        print("1:D3,  2:D6,  3:D10,  4:D20")
        desiredDice = input()
    
    totalRolls = []
    amountOfRolls = ''
    
    while amountOfRolls <= '0':
        print("Pick desired amount of rolls")
        playerInput = input()
        if playerInput[0] in "1 2 3 4 5 6 7 8 9 0".split():
            amountOfRolls = playerInput

    totalRolls = getRandomRolls(int(amountOfRolls), int(desiredDice))
    print("You rolled...: ", end = '')
    for i in range(len(totalRolls)):
        print(totalRolls[i], end = ' ')
    print()
    print('Would you like to roll again?')
    if not input().lower().startswith('y'):
       sys.exit()
    
    


