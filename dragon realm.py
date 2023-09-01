#Dragon realm game, finished 7/9/2023.
import random
import time

def displayIntro():
    print('''You are in a magical land full of dragons.\nIn front of you lies two caves. \nIn one cave, the dragon is friendly and will bestow his treasure upon you. \nHowever, the other dragon is greedy and hungry and will feast upon you.''')
    print()

def choseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you choose? (1 or 2)')
        cave = input()
        
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print('A large dragon jumps out in front of you! It opens its jaws wide and...')
    print('')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if(chosenCave == str(friendlyCave)):
            print('Gives you all his treasure!')
    else:
            print('Gobbles you whole!')
            
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'Y':
        displayIntro()
        caveNumber = choseCave()
        checkCave(caveNumber)

        print('Do you wish to play again?')
        playAgain = input()
