board = [
   ['A','B','C','E'],
   ['S','F','C','S'],
   ['A','D','E','E'],
]

# Your task is to write a function that takes a word as input and determines whether or not the
# word exists on the board. Here are some examples:
#
# word = "ABCCED", returns true
# word = "SEE", returns true
# word = "ABCB", returns false
# word = "ABCESCFSADEE", returns true

def exists(word: str) -> bool:
    for cell in _get_cells(board):
        if _exists_starting_at_cell(cell, word, set()):
            return True
    return False


def _get_cells(board):
    nrows, ncols = len(board), len(board[1])
    return [(i, j) for i in range(len(board)) for j in range(len(board[0]))]


def _get_value(cell, board):
    return board[cell[0]][cell[1]]


def _exists_starting_at_cell(cell, word, visited):
    if not word:
        return True
    if word[0] != _get_value(cell, board):
        return False
    print(cell, _get_value(cell, board), visited)
    visited.add(cell)
    for neighbor in _get_neighbors(cell, board):
        if neighbor not in visited and _exists_starting_at_cell(neighbor, word[1:], visited):
            return True
    return False


def _get_neighbors(cell, board):
    nrows, ncols = len(board), len(board[1])
    i, j = cell
    for delta_x in [-1, 1]:
        if 0 <= i + delta_x < nrows:
            yield (i + delta_x, j)
    for delta_y in [-1, 1]:
        if 0 <= j + delta_y < ncols:
            yield (i, j + delta_y)

# print(exists("ABCCED"), True)
# print(exists("SEE"), True)
# print(exists("ABCB"), False)
print(exists("ABCESCFSADEE"), True)
