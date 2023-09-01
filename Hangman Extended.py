#Hangman Game Extended, 7/13/2023
import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  0   |
      |
      |
     ===''', '''
  +---+
  0   |
  |   |
      |
     ===''', '''
  +---+
  0   |
 /|   |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
 /    |
     ===''', '''
  +---+
  0   |
 /|\  |
 / \  |
     ===''', '''
  +---+
  0   |
 /|\  |
_/ \  |
     ===''', '''
  +---+
  0   |
 /|\  |
_/ \_ |
     ===''']

words = {'animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
         'shapes' : 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'fruits' : 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalopue mango strawberry tomato'.split()}

def getRandomWord(wordDict):
    #This function returns a random string from the passed dictionary of strings
    #First, select a random key from the dictionary
    wordKey = random.choice(list(wordDict.keys()))
    #Second, randomly return a word from the key's list in the dictionary
    wordIndex = random.randint(0, len(wordDict[wordKey])- 1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #Replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Show the secret word with spaces in between each letter.
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):
    #Returns the letter the player entered. This function also makes sure the player entered a single letter and not a repeat
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Guess a single letter only')
        elif guess in alreadyGuessed:
            print('You have already guessed this letter. Choose another')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Enter a letter')
        else:
            return guess

def playAgain():
    #This function returns true if the player wants to play again.
    print('Do you want to play again? (Yes or No)')
    return input().lower().startswith('y')

#Beginning of the game
print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
    print('Enter difficulty: E = Easy, M = Medium, H = Hard')
    difficulty = input().upper()

if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
elif difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[6]
    del HANGMAN_PICS[5]

    
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    print('The difficulty is: ' + difficulty)
    displayBoard(missedLetters, correctLetters, secretWord)

    #Let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord: #Player guessed correctly
        correctLetters = correctLetters + guess

        #Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
        if foundAllLetters:
            print('Congrats! The secret word is "' + secretWord + '"! You win!')
            gameIsDone = True
    else: #Player guessed incorrectly
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed letters and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + str(secretWord) +'"')
            gameIsDone = True
    
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
       



    
