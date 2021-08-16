from copy import deepcopy


def white_can_win_in_n_moves(n, board):
    for moves in possible_moves(n, board):
        if white_wins(moves):
            return True
    return False


# "path" is a list of boards.
# A "board" is a dict like board1 below.



def possible_moves(n, board):
    """
    List all possible sequences of moves of length <= n.
    """
    print(f'initial board:      {board}')
    return gather_paths(board, n, 0)


def gather_paths(board, n_max, n):
    """
    Return list of all possible moves starting from `board`.
    """
    paths = []
    if n == n_max:
        return paths
    for white_child in get_white_children(board):
        print(f'after white move {n}: {white_child}')
        paths.append([board] + [white_child])
        for black_child in get_black_children(white_child):
            print(f'after black move {n}: {black_child}')
            for child_path in gather_paths(black_child, n_max, n+1):
                paths.append([board] + [white_child] + [black_child] + child_path)
    return paths



def get_white_children(board):
    """
    Return all boards that can be generated from `board` via 1 white move.
    """
    return get_moves('w', board)




def get_black_children(board):
    """
    Return all boards that can be generated from `board` via 1 black move.
    """
    return get_moves('b', board)


def get_moves(who, board):
    moves = []
    moves.extend(do_pawn_moves(who, board))
    try:
        moves.append(do_queen_move(who, board))
    except AssertionError:
        pass

    return moves

def do_queen_move(who, board):
    for i, piece in enumerate(board[who]):
        if piece.startswith("Q"):
            return move_queen(who, i, board)
    raise AssertionError


def move_queen(who, i, board):
    # print(f'move_queen: {who} {i} {board}')
    piece, col, row = board[who][i]
    row = int(row)
    in_front = f'{col}{row+1}'
    behind = f'{col}{row-1}'

    if row <= 4 and not any(piece.endswith(in_front) for piece in board[who] for who in ['w', 'b']):
        # print('moving Q forwards')
        board = deepcopy(board)
        board[who][i] = f'{piece}{col}{row+1}'
        return board
    if row >= 2 and not any(piece.endswith(behind) for piece in board[who] for who in ['w', 'b']):
        # print('moving Q backwards')
        board = deepcopy(board)
        board[who][i] = f'{piece}{col}{row-1}'
        return board
    raise AssertionError


def do_pawn_moves(who, board):
    moves = []
    for i, piece in enumerate(board[who]):
        if piece.startswith("P"):
            try:
                moves.append(move_pawn(who, i, board))
            except AssertionError:
                pass
    return moves


def move_pawn(who, i, board):
    piece, col, row = board[who][i]
    row = int(row)
    assert row <= 4
    in_front = f'{col}{row+1}'
    assert not any(piece.endswith(in_front) for piece in board[who] for who in ['w', 'b'])

    board = deepcopy(board)
    board[who][i] = f'{piece}{col}{row+1}'
    return board


def white_wins(path):
    """
    Return True iff `moves` ends in a win for white.
    """
    return not any(piece.startswith('Q') for piece in path[-1]['b'])




board1 = {
    'w': ['QB1','PB3'],
    'b': ['QA4']
}
board2 = {
    'w': ['QB1','PB3'],
    'b': ['QA3']
}

from pprint import pprint
pprint(possible_moves(1, board1))

# assert white_can_win_in_n_moves(1, board1) == True
# assert white_can_win_in_n_moves(2, board2) == True
# assert white_can_win_in_n_moves(1, board2) == False
