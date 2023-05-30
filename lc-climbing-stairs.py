# https://leetcode.com/problems/climbing-stairs


from math import sqrt


class Solution:
    def climbStairs(self, n: int) -> int:
        # It is fib
        n = n + 1
        return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (sqrt(5) * 2 ** n))
        # return n_paths(n)


_cache = {}


def memoized(f):
    def g(*args):
        key = tuple(args)
        if key not in _cache:
            _cache[key] = f(*args)
        return _cache[key]

    return g


@memoized
def n_paths(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n_paths(n - 1) + n_paths(n - 2)
