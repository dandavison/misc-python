# https://leetcode.com/problems/generate-parentheses


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # given a well-formed expression, a new pair can be
        # (i) inserted at any position
        # (ii) wrapped around every open-close pair
        # E.g. n = 3
        # we start with ()
        # applying (i) yields
        # ()() (())
        # applying (ii) yields
        # (())
        # deduplicating yields
        # ()() (())
        # Now using our 3rd pair with (i) yields
        # ()()() ()(()) ((()))
        # alternatively (ii) yields
        # (())() ()(()) (()()) ((()))
        # deduplicating yields
        # ()()() ()(()) ((())) (())() (()())
        # which matches the example
        return generate(["()"], n - 1) if n else []
    

def generate(expressions, n):
    if not n:
        return expressions
    new_exprs = set()
    for e in expressions:
        new_exprs.update(_generate_transformations(e))
    return generate(list(new_exprs), n - 1)


def _generate_transformations(e):
    stack = []
    for j, c in enumerate(e):
        # insertion
        yield e[:i] + "()" + e[i:]
        # wrapping
        if c == "(":
            stack.append(j)
        elif c == ")":
            i = stack.pop()
            yield e[:i] + "(" + e[i:j+1] + ")" + e[j+1:]
