import shutil


def generate_board(n: int, board_size: int, input_string: str):
    '''Generate a nxn game board.'''
    input_string = list(input_string)
    board = []
    for i in range(n):
        inner_board = []
        for j in range(n):
            inner_board.append(input_string.pop(0))
        board.append(inner_board)

    columns = shutil.get_terminal_size().columns

    print("\n")
    print("--- Game Board ---".center(columns))
    for layer in board:
        print(str(layer).center(columns))
    print("\n")

    return board
