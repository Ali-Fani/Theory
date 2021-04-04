from collections import Counter
import platform
from os import system
from rich import print
from random import choice
import time
from math import inf as infinity
PLAYER1 = -1
PLAYER2 = +1
pve = False
state = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def reset():
    global state
    state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


def evaluate(state):
    """Function to detrmain winner

    Args:
        state (2D Array): Current state of the state

    Returns:
        int: Returns +1 for computer -1 for human and 0 for draw
    """
    if wins(state, PLAYER1):
        score = PLAYER1
    elif wins(state, PLAYER2):
        score = PLAYER2
    else:
        score = 0
    return score


def wins(state, player):
    """Checks For win in Row,Column,diagonals,Anti-diagonal

    Args:
        state (2d array): Current state of board
        player (int): Player to Check if wins

    Returns:
        Bool: Returns True if player won and false if not
    """
    diag1 = []
    diag2 = []
    winCondition = [player]*3
    for i in range(len(state)):
        if (state[i][0] == player and state[i][1] == player
                and state[i][2] == player):
            return True
        if (state[0][i] == player and state[1][i] == player
                and state[2][i] == player):
            return True
    for x in range(len(state)):
        for y in range(len(state)):
            if x == y:
                diag1.append(state[x][y])
            if (x+y) == (len(state)-1):
                diag2.append(state[x][y])
    if (Counter(diag1) == Counter(winCondition)
            or Counter(diag2) == Counter(winCondition)):
        return True
    return False


def game_over(state):
    """Checks if any of sides Won

    Args:
        state (2d Array): Current state of board

    Returns:
        [bool]: True if any of sides won
    """
    return wins(state, PLAYER1) or wins(state, PLAYER2)


def empty_cells(state):
    """Returns Empty Cells of Current Board

    Args:
        state (2D Array): Current state of board

    Returns:
        List: List of Empty Cells in Board
    """
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells


def valid_move(x, y):
    """Checked if coordination are empty and valid

    Args:
        x (int): coordination x
        y (int): coordination y

    Returns:
        Bool: Returns True if coordination is empty and valid
    """
    if [x, y] in empty_cells(state):
        return True
    else:
        return False


def set_move(x, y, player):
    """Makes player move after validating move

    Args:
        x (INT): coordination X
        y (INT): coordination y
        player (INT): Player id to put in Board

    Returns:
        [type]: [description]
    """
    if valid_move(x, y):
        state[x][y] = player
        return True
    else:
        return False


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, p1_choice, p2_choice):
    """Renders Current state of board in terminal

    Args:
        state (2D Array): Current state of Board
        p1_choice (str): Character of player 1
        p2_choice (str): Character of player 2
    """
    chars = {
        -1: p1_choice,
        +1: p2_choice,
        0: ' '
    }
    str_line = '---------------'
    print("\n"+str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            if(symbol == "X"):
                print(f'| [red]{symbol}[/red] |', end='')
            elif symbol == "O":
                print(f'| [blue]{symbol}[/blue] |', end='')
            else:
                print(f'| [white]{symbol}[/white] |', end='')
        print('\n'+str_line)


def p_turn(player):
    """Gets player input,validate and make 
    the move and at the end checks for winner

    Args:
        player (INT): Player id to make move
    """
    p_choice = {
        PLAYER1: "X",
        PLAYER2: "O"
    }

    depth = len(empty_cells(state))
    if depth == 0 or game_over(state):
        return
    move = - 1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Player {p_choice[player]} turn ')
    render(state, p_choice[PLAYER1], p_choice[PLAYER2])
    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], player)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == PLAYER2:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == PLAYER2:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def ai_turn():
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    """
    p_choice = {
        PLAYER1: "X",
        PLAYER2: "O"
    }
    depth = len(empty_cells(state))
    if depth == 0 or game_over(state):
        return

    clean()
    print(f'Computer turn [{p_choice[PLAYER2]}]')
    render(state, p_choice[PLAYER1], p_choice[PLAYER2])

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(state, depth, PLAYER2)
        x, y = move[0], move[1]

    set_move(x, y, PLAYER2)
    time.sleep(1)


def main():
    player1 = 0
    player2 = 0
    draw = 0
    computer = 0
    p1_choice = "X"
    p2_choice = "O"
    usage = """
Wellcome to TIC TAC TOE game
1- User VS User
2- User VS PC
3- Exit\n"""
    while True:
        userInput = int(input(usage))
        if userInput == 1:
            start = time.time()
            clean()

            while len(empty_cells(state)) > 0 and not game_over(state):
                p_turn(PLAYER1)
                p_turn(PLAYER2)
            if wins(state, PLAYER1):
                clean()
                render(state, p1_choice, p2_choice)
                player1 += 1
                print(f'Player {p1_choice} Won!')
                print(f"Player X won : {player1} times")
                print(f"Player O won : {player2} times")
                print(f"Game tied : {draw} times")

            elif wins(state, PLAYER2):
                clean()
                render(state, p1_choice, p2_choice)
                player2 += 1
                print(f'Player {p2_choice} Won!')
                print(f"Player X won : {player1} times")
                print(f"Player O won : {player2} times")
                print(f"Game tied : {draw} times")
            else:
                clean()
                render(state, p1_choice, p2_choice)
                draw += 1
                print('DRAW!')
                print(f"Player X won : {player1} times")
                print(f"Player O won : {player2} times")
                print(f"Game tied : {draw} times")
            end = time.time()
            reset()
            print(f"Time taken for this game is {end-start}")
        if userInput == 2:
            start = time.time()
            clean()

            while len(empty_cells(state)) > 0 and not game_over(state):
                p_turn(PLAYER1)
                ai_turn()
            if wins(state, PLAYER1):
                clean()
                render(state, p1_choice, p2_choice)
                player1 += 1
                print(f'Player {p1_choice} Won!')
                print(f"Player X won : {player1} times")
                print(f"Computer won : {computer} times")
                print(f"Game tied : {draw} times")
            elif wins(state, PLAYER2):
                clean()
                render(state, p1_choice, p2_choice)
                computer += 1
                print(f'Player {p2_choice} Won!')
                print(f"Player X won : {player1} times")
                print(f"Computer won : {computer} times")
                print(f"Game tied : {draw} times")
            else:
                clean()
                render(state, p1_choice, p2_choice)
                draw += 1
                print('DRAW!')
                print(f"Player X won : {player1} times")
                print(f"Computer won : {computer} times")
                print(f"Game tied : {draw} times")
            end = time.time()
            reset()
            print(f"Time taken for this game is {end-start}")
        if userInput == 3:
            exit()


if __name__ == '__main__':
    main()
