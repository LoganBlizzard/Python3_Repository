#Bagels deduction game 7/17/2023
import random

NUM_DIGITS = 3
MAX_GUESS = 10

def GetSecretNum():
    #Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def GetClues(guess, secretNum):
    #Returns a string with the Pico, Fermi & Bagles clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
            
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)

def IsOnlyDigits(num):
    #Returns True if num is a string of only digits. Otherwise, returns Fales.
    if num == '':
        return False
    for i in num:
        if i not in '1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

print('I am thinking of a %s-digit number. Try to guess what it is.' %(NUM_DIGITS))
print('The clue I give are...')
print('When I say:    That means:')
print('     Bagles    None of the digits is correct')
print('     Pico      One digit is correct but in the WRONG position')
print('     Fermi     One digit is correct AND in the RIGHT position')

while True:
    secretNum = GetSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' %(MAX_GUESS))
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not IsOnlyDigits(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()
        print(GetClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
        
    
