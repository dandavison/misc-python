# 3[a2[c]]
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_op = ""
        curr_arg = ""
        in_arg = False

        print(s)
        print()
        for c in s:
            print(c, "->", end=" ")
            if c == "[":
                stack.append(curr_op)
                curr_op = ""
            elif c == "]":
                if curr_arg:
                    stack.append(curr_arg)
                    curr_arg = ""
                arg = stack.pop()
                op = stack.pop()
                stack.append(arg * int(op))
            elif c in "0123456789":
                if in_arg:
                    if curr_arg:
                        stack.append(curr_arg)
                        curr_arg = ""
                    in_arg = False
                curr_op += c
            else:
                in_arg = True
                curr_arg += c

            print(stack)

        return "".join(stack)


if __name__ == "__main__":
    print(Solution().decodeString("3[a]2[bc]"))
    print(Solution().decodeString("3[a2[c]]"))
