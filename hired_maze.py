def solution(maze, n):
    if maze[0][0] != 0:
        return False
    has_path = {(0, 0)}
    for level in range(1, 2 * n):
        for i, j in get_diagonal_coords(level, n):
            # This condition looks inelegant
            if i < n and j < n and maze[i][j] != 0:
                continue
            for k, l in get_neighbors(i, j):
                if (k, l) in has_path:
                    has_path.add((i, j))
                    break

    return (n - 1, n - 1) in has_path


def get_neighbors(i, j):
    if i > 0:
        yield (i - 1, j)
    if j > 0:
        yield (i, j - 1)


def get_diagonal_coords(level, n):
    if level < n:
        i, j = (level, 0)
    else:
        i, j = (n - 1, level - n + 1)
    while i >= 0:
        yield (i, j)
        i -= 1
        j += 1
