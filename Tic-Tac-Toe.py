#Tic-Tac-Toe 7/14/2023

import random

def DrawBoard(board):
    #This function prints out the board that was passed

    #'board' is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('- + - + -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- + - + -')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

def InputPlayerLetter():
    #Lets the player type which letter they want to be.
    #Returns a list with the player's letter as the first item and the...
    #...computers letter as second
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you wish to be "X" or "O"?')
        letter = input().upper()

    #The first element is the player's letter, second is computer
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def WhoGoesFirst():
    #Randomly choose which player goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def MakeMove(board, letter, move):
    board[move] = letter

def IsWinner(board, letter):
    #Given a board and a player's letter, this function returns true...
    #...if that player has won
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or #Across top
    (board[4] == letter and board[5] == letter and board[6] == letter) or #Across Middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or #Across bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or #Down Left
    (board[8] == letter and board[5] == letter and board[2] == letter) or #Down Mid
    (board[9] == letter and board[6] == letter and board[3] == letter) or #Down Right
    (board[7] == letter and board[5] == letter and board[3] == letter) or #Diagnol
    (board[9] == letter and board[5] == letter and board[1] == letter))

def GetBoardCopy(board):
    #Make a copy of the board list and return it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def IsSpaceFree(board, move):
    #Return true if passed move is free on the passed board
    return board[move] == ' '

def GetPlayerMove(board):
    #Let the player enter their move.
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
        return int(move)

def ChooseRandomMoveFromList(board, movesList):
    #Returns a valid move from the passed list on the passed board.
    #Returns on if there is no valid move
    possibleMoves = []
    for i in movesList:
        if IsSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def GetComputerMove(board, computerLetter):
    #Given a board and the computer's letter, determine where to move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
    #The algorithm for Tic-Tac-Toe AI:
    #First, check if we can win in the next move and return that spot
    for i in range (1, 10):
        boardCopy = GetBoardCopy(board)
        if(IsSpaceFree(boardCopy, i)):
            MakeMove(boardCopy, computerLetter, i)
            if IsWinner(boardCopy, computerLetter):
                return i

    #Check if the player can win in the next move and return that spot
    for i in range(1, 10):
        boardCopy = GetBoardCopy(board)
        if IsSpaceFree(boardCopy, i):
            MakeMove(boardCopy, playerLetter, i)
            if IsWinner(boardCopy, playerLetter):
                return i

    #Try to take a corner if they are free
    move = ChooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move!= None:
        return move

    #Try to take center if its free
    if IsSpaceFree(board, 5):
        return 5

    #Move on one of the sides
    return ChooseRandomMoveFromList(board, [2, 4, 6, 8])

def IsBoardFull(board):
    #Return True if every space on the board has been taken. Otherwise return False
    for i in range(1, 10):
        if IsSpaceFree(board, i):
            return False
    else:
        return True

#The Game Loop
print("Welcome to Tic-Tac-Toe!")

while True:
    #Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = InputPlayerLetter()
    turn = WhoGoesFirst()
    print('The ' + turn + ' will go first')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #Players Turn
            DrawBoard(theBoard)
            move = GetPlayerMove(theBoard)
            MakeMove(theBoard, playerLetter, move)

            if IsWinner(theBoard, playerLetter):
                DrawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if IsBoardFull(theBoard):
                    DrawBoard(theBoard)
                    print('The game is a tie!')
                    break
            
                else:
                    turn = 'computer'

        else:
            #Computers Turn
            move = GetComputerMove(theBoard, computerLetter)
            MakeMove(theBoard, computerLetter, move)

            if IsWinner(theBoard, computerLetter):
                DrawBoard(theBoard)
                print('The computer has beaten you, Game Over')
                gameIsPlaying = False
            else:
                if IsBoardFull(theBoard):
                    DrawBoard(theBoard)
                    print('The game is a tie!')
                    break
            
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
            
            
            
            
                    
            
