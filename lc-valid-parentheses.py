# https://leetcode.com/problems/valid-parentheses

# Passes all tests
class Solution:
    def isValid(self, s: str) -> bool:
        openers = "({["
        closers = ")}]"
        opener2closer = dict(zip(openers, closers))

        stack = []
        for c in s:
            closer = opener2closer.get(c)
            if closer:
                stack.append(closer)
            else:
                if not stack or stack.pop() != c:
                    return False
        return not bool(stack)

class Solution2:
    def isValid(self, s: str) -> bool:
        opener2closer = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        for c in s:
            if closer := opener2closer.get(c):
                stack.append(closer)
            else:
                if not stack or stack.pop() != c:
                    return False
        return bool(not stack)
