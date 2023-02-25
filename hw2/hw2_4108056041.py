# Initial values of Alpha and Beta
MAX, MIN = 1000, -1000
player, opponent = 'X', 'O'


# if moves left
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] != 'X' and board[i][j] != 'O'):
                return True
    return False


# Determine if this move makes a tie or win
def ifWin(board):
    # Checking for Columns for X or O victory.
    for col in range(3):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]):
            return True

    # Checking for Rows for X or O victory.
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            return True

    # Checking for Diagonals for X or O victory.
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return True

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return True

    # Else if none of them have won then return 0
    return False


# This is the evaluation function
def evaluate(b):
    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if (b[0][0] == player):
            return 10
        elif (b[0][0] == opponent):
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if (b[0][2] == player):
            return 10
        elif (b[0][2] == opponent):
            return -10

    # Checking for Rows for X or O victory.
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == player):
                return 10
            elif (b[row][0] == opponent):
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3):
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
            if (b[0][col] == player):
                return 10
            elif (b[0][col] == opponent):
                return -10

    # Else if none of them have won then return 0
    return 0


# minimax function.
# Alpha-Beta Pruning version
def minimax(board, depth, isMax, alpha, beta):
    score = evaluate(board)

    # If Maximizer has won the game return
    # evaluated score
    if (score == 10):
        return score - depth

    # If Minimizer has won the game return
    # evaluated score
    if (score == -10):
        return score + depth

    # If there are no more moves and no winner then
    # it is a tie
    if (isMovesLeft(board) == False):
        return 0

    # If this maximizer's move
    if (isMax == True):
        best = MIN

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] != 'X' and board[i][j] != 'O'):

                    # Make the move
                    temp = board[i][j]
                    board[i][j] = player

                    # Call minimax recursively and choose
                    # the maximum value
                    val = minimax(board, depth+1, False, alpha, beta)
                    best = max(best, val)
                    alpha = max(alpha, best)

                    # Undo the move
                    board[i][j] = temp

                    # Alpha Beta Pruning
                    if beta <= alpha:
                        break

        return best

    # If this minimizer's move
    else:
        best = MAX

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] != 'X' and board[i][j] != 'O'):

                    # Make the move
                    temp = board[i][j]
                    board[i][j] = opponent

                    # Call minimax recursively and choose
                    # the minimum value
                    val = minimax(board, depth+1, True, alpha, beta)
                    best = min(best, val)
                    beta = min(beta, best)

                    # Undo the move
                    board[i][j] = temp

                    # Alpha Beta Pruning
                    if beta <= alpha:
                        break

        return best

# This will return the best possible move for the player


def findBestMove(board):
    bestVal = MIN
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):

            # Check if cell is empty
            if (board[i][j] != 'X' and board[i][j] != 'O'):

                # Make the move
                temp = board[i][j]
                board[i][j] = player

                # compute evaluation function
                moveVal = minimax(board, 0, False, MIN, MAX)

                # Undo the move
                board[i][j] = temp

                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove


# show board
def showBoard(board):
    for i in range(3):
        j = 0
        print("| %c | %c | %c |" % (board[i][j], board[i][j+1], board[i][j+2]))


# Driver code
if __name__ == "__main__":
    i = 0
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

    while (True):
        # real Player's turn
        if (isMovesLeft(board) == False):
            print("moves is left")
            break

        print("\nround %d :" % i)
        i += 1
        showBoard(board)
        enter = input("Your move : ")
        realPlayer = int(enter)
        realPlayer -= 1
        row = realPlayer // 3
        col = realPlayer % 3

        if (realPlayer == -1):
            print("enter 0 -> exit the game")
            break
        elif (board[row][col] == 'X' or board[row][col] == 'O'):
            print("can't enter this, exit the game, too")
            break
        else:
            board[row][col] = 'X'

        if (ifWin(board) == True):
            print("\nreal Player win!! yayaya")
            showBoard(board)
            print("\n")
            break

        # ai Player's turn
        print("\nround %d :" % i)
        i += 1
        showBoard(board)
        if (isMovesLeft(board) == False):
            print("The game is a tie!")
            break
        bestMove = findBestMove(board)
        aiPlayer = 3 * bestMove[0] + bestMove[1] + 1
        print("\nAi's move : %d" % aiPlayer)
        board[bestMove[0]][bestMove[1]] = 'O'

        if (ifWin(board) == True):
            print("ai Player win!! ohno")
            showBoard(board)
            print("\n")
            break


# The real player can enter 0 at any time to exit the game............................................................................................................
# 1 8 4 9
# 5 7 2 6 9
# 1 3 8 4
