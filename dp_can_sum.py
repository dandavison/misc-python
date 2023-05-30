from typing import List


def can_sum(target: int, numbers: List[int]) -> bool:
    """
    N := |numbers|
    Time: N^2 (because N + N-1 + ... + 1 = N(N-1) / 2)
    Space: N

    >>> can_sum(0, [])
    True
    >>> can_sum(1, [])
    False
    >>> can_sum(0, [0])
    True
    >>> can_sum(1, [0])
    False
    >>> can_sum(0, [1])
    False
    >>> can_sum(1, [1])
    True
    >>> can_sum(1, [0, 1])
    True
    >>> can_sum(2, [0, 1])
    False
    >>> can_sum(2, [1, 2])
    False
    >>> can_sum(3, [1, 2])
    True
    """
    # numbers can sum to target if numbers \ {numbers[i]} can sum to target - numbers[i]
    if target < 0:
        return False
    if not numbers:
        return target == 0
    for i in range(len(numbers)):
        number_i = numbers[i]
        if can_sum(target - number_i, numbers_without_i):
            return True
    return False
