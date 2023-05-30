# - Grid of dimensions m x n
# - Start in top left
# - How many ways to bottom right?
# - Can only move down or right

# We must move m down and n right.
# - Therefore number of different ways is number of distinct binary strings containing m 1s and n 0s.
# - This is (m + n) choose m
# - Recall that N choose K is N(N-1)...(N - K + 1) / K! = N!/[K! (N-K)!]
# - So answer is (m + n)! / m! n!
import math
import sys

_memoize_dict = {}


def memoize(f):
    def wrapped(*args):
        key = tuple(args)
        if key not in _memoize_dict:
            _memoize_dict[key] = f(*args)
        return _memoize_dict[key]

    return wrapped


@memoize
def count_paths(m: int, n: int):
    # time: 2^(m + n)
    # space: (m + n)
    if m == 1 and n == 1:
        return 1
    else:
        paths = 0
        if m > 1:
            paths += count_paths(m - 1, n)
        if n > 1:
            paths += count_paths(m, n - 1)
        return paths


def closed_form(m: int, n: int):
    # time and space O(1)
    fact = math.factorial
    return fact(m - 1 + n - 1) / (fact(m - 1) * fact(n - 1))


if __name__ == "__main__":

    m, n = map(int, sys.argv[1:])
    print(m, n)
    print(closed_form(m, n))
    print(count_paths(m, n))
