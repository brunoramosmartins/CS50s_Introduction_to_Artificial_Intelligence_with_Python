"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    Retorna o jogador que tem a próxima vez de jogar em um tabuleiro.
    """

    # By exploring the parity of the moves, we can determine whose turn it is.
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                count += 1
    if count % 2 == 0: return X
    else: return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    Retorna o conjunto de todas as ações possíveis (i, j) disponíveis no tabuleiro.
    """

    _actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY: _actions.add((i, j))
    return _actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Retorna o tabuleiro resultante ao fazer a jogada (i, j) no tabuleiro.
    """

    results = copy.deepcopy(board)
    results[action[0]][action[1]] = player(board)
    return results


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != EMPTY: return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != EMPTY: return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != EMPTY: return board[2][0]

    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != EMPTY: return board[0][0]
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != EMPTY: return board[0][1]
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != EMPTY: return board[0][2]

    elif board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != EMPTY: return board[0][0]
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != EMPTY: return board[0][2]

    else: return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if (winner(board) == X): return True
    elif (winner(board) == O): return True
    elif len(actions(board)) != 0: return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]

def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];
