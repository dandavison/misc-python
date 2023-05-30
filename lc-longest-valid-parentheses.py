# https://leetcode.com/problems/longest-valid-parentheses/

# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.

# times out


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return move_right_forming_valid_exprs(s)


def move_right_forming_valid_exprs(s):
    _max = 0
    i = 0
    while True:
        if i >= len(s):
            return _max
        k = _max_length(s[i:])
        # print(i, s[i:], k)
        if k:
            i += k
            _max = max(_max, k)
        else:
            i += 1


def _max_length(s):
    _max = 0
    balance = 0
    for i, c in enumerate(s):
        if c == "(":
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            _max = i + 1
        elif balance < 0:
            _max = i
            break
    return _max


f = Solution().longestValidParentheses
print(f("()()"))


def stack_of_start_indices(s):
    # Not correct yet
    # Returns 4 instead of 6 for "(())()"
    _max = 0
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            if stack:
                start = stack.pop()
                _max = max(i - start + 1, _max)
            else:
                # expression has become invalid
                stack = []
    return _max


def dict_of_start_positions(s):
    _max = 0
    balances = {}
    for j, c in enumerate(s):
        if c == "(":
            balances[j] = 0
            for start in balances:
                balances[start] += 1
        else:
            for start in list(balances):
                balances[start] -= 1
                if balances[start] == 0:
                    # Reached end of a valid expression; the expression may
                    # continue however
                    _max = max(_max, j - start + 1)
                elif balances[start] < 0:
                    # expression starting at `start` has become invalid; it
                    # cannot recover
                    del balances[start]
        # print(j, c, balances)

    return _max
