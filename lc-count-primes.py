# https://leetcode.com/problems/count-primes


class Solution:
    # These implementations time out on leetcode
    def countPrimes(self, n: int) -> int:
        # n is a prime if its only factors are 1 and n.
        # primes are 2, 3, 5, 7, 11, ...
        primes = set(range(2, n))
        for i in range(2, n // 2 + 1):
            if i in primes:
                # primes -= {k * i for k in range(2, n // i + 1)}
                for k in range(2, n // i + 1):
                    try:
                        primes.remove(i*k)
                    except KeyError:
                        pass
        return len(primes)

f = Solution().countPrimes
for i in range(11):
    print(i, f(i))
