from collections import deque


def solution(src, dest):
    src, dest = map(index_to_coord, (src, dest))  # type: ignore
    grid = set(map(index_to_coord, range(64)))

    moves = [1 + 2j, 2 + 1j, 2 - 1j, 1 - 2j, -1 - 2j, -2 - 1j, -2 + 1j, -1 + 2j]
    queue, visited = deque([src]), {src}
    steps = 0
    while queue:
        for _ in range(len(queue)):
            cell = queue.popleft()
            if cell == dest:
                return steps
            elif cell not in grid:
                continue
            else:
                for move in moves:
                    next_cell = cell + move
                    if next_cell not in visited:
                        queue.append(next_cell)
                        visited.add(next_cell)
        steps += 1
    assert False, "Impossible"


def index_to_coord(idx):
    x, y = divmod(idx, 8)
    return x + y * 1j


def coord_to_index(coord):
    return 8 * int(coord.real) + int(coord.imag)


# print(solution(19, 36))
