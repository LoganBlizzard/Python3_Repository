#Reversegam: A clone of Othello/Reversi 8/3/23

import random
import sys

WIDTH = 8 #Board is 8 spaces wide
HEIGHT = 8 #Board is 8 spaces high

def drawBoard(board):
    # Print the board passed to this function. Return None.
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' %(y+1), end = '')
        for x in range(WIDTH):
            print(board[x][y], end = '')
        print('|%s' %(y+1))
    print(' +--------+')
    print('  12345678')

def getNewBoard():
    #Create a brand new, blank board data structure.
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',])
    return board

def isValidMove(board, tile, xstart, ystart):
    #Return false if the player chose a invalid move
    #If it is a valid move, return a list of spaces that would become the...
    #Players if they made a move
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1, 0], [-1,1]]:
        x, y = xstart, ystart
        x += xdirection #First step in x direction
        y += ydirection #first step in y direction
        while isOnBoard(x,y) and board[x][y] == otherTile:
            #keep moving in this direction
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                #There are pieces to flip over. Go in the reverse direction until we reach original space
                #Noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x,y])
    if len(tilesToFlip) == 0: #If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip

def isOnBoard(x, y):
    #Return True if the coordinates are located on the board.
    return x>=0 and x <= WIDTH - 1 and y>= 0 and y <= HEIGHT - 1

def getBoardWithValidMoves(board, tile):
    #Return a new board with periods marking the valid moves the player can make.
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    #Return a list of [x,y] lists of valid moves for the given player on the given board.
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x,y])
    return validMoves

def getScoreOfBoard(board):
    #Determine the score by counting the tiles. Return a dictionary with keys 'X' and 'O'
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X' :xscore, 'O' :oscore}

def enterPlayerTile():
    #Let the player enter which tile they want to be.
    #Return a list with the players tile as the first item and the computers...
    #tile as the second
    print('What tile do you wish to be? (X or O)')
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        tile = input().upper()

    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, tile, xstart, ystart):
    #Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces
    #Return False if this is an invalid move; True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    #Make a duplicate of the board list and return it.
    boardCopy = getNewBoard()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] =  board[x][y]
    return boardCopy

def isOnCorner(x, y):
    #Return True if the position is in on eof the four corners.
    return (x== 0 or x == WIDTH - 1) and (y==0 or y == HEIGHT - 1)

def getPlayerMove(board, playerTile, computerTile):
    #Let the player enter their move.
    #Return the move as [x, y] (or return the strings 'hints' or 'quit'
    DIGITS1T08 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints')
        move = input().lower()
        if move == 'quit' or move == 'hints':
            return move

        if len(move) == 2 and move[0] in DIGITS1T08 and move[1] in DIGITS1T08:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Enter the column "y" (1-8) and then the row "x" (1-8)')

            
    return [x,y]

def getComputerMove(board, computerTile):
    #Given a board and the computer's tile, determine where to move and return...
    #that move as an [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves) #Randomize the order of the moves
    #Always go for a corner if available
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    #Find the highest-scoring move possible.
        bestScore = -1
        for x, y in possibleMoves:
            boardCopy = getBoardCopy(board)
            makeMove(boardCopy, computerTile, x, y)
            score = getScoreOfBoard(boardCopy)[computerTile]
            if score > bestScore:
                bestMove = [x, y]
                bestScore = score
        return bestMove

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('You: %s points. Computer: %s points.' % (scores[playerTile], scores[computerTile]))
    
def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    #Clear the board and place starting pieces.
    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board #no one can move, so end game
        elif turn == 'player': #Players Turn
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile, computerTile)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()#Quit the game
                elif move == 'hints':
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'computer'

        elif turn == 'computer': #Computers Turn
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)

                input('Press Enter to see the computer\'s move.')

                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = 'player'


print('Welcome to Reversegram!')

playerTile, computerTile = enterPlayerTile()
while True:
    finalBoard = playGame(playerTile, computerTile)

    #Display the final score
    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X scored %s points. O scored %s points' %(scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('Congragulations! You beat the computer by %s points!' %(scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('Bummer, you lost. The computer beat you by %s points.' %(score[computerTile] - score[playerTile]))
    
    else:
        print('The game was a tie!')

    print('Do you want to play again? (yes or no')
    if not input().lower().startswith('y'):
        break
    

    
