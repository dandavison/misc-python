def solution(n):
    return list(_solution)

def _solution(n):
    for f in fib(n):
        if is_prime(f):
            yield f

def is_prime(n):
    k = n // 2
    while k > 1:
        q, r = divmod(n, k)
        if r == 0:
            return False
        k -= 1
    return n > 1


def fib(n):
    f1, f2 = (1, 1)
    if n >= 1:
        yield f1
    if n >= 2:
        yield f2
    n -= 2
    while n > 0:
        f1, f2 = (f2, f1 + f2)
        yield f2
        n -= 1
