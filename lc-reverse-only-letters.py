# https://leetcode.com/problems/reverse-only-letters


from collections import deque


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        alpha_min, alpha_max = ord("A"), ord("z")

        # Form two sorted streams
        alpha = deque([])
        non_alpha = []
        for i, c in enumerate(s):
            if alpha_min <= ord(c) <= alpha_max:
                alpha.appendleft((n - i - 1, c))
            else:
                non_alpha.append((i, c))

        # Merge the character components of the streams
        return "".join(_merge_streams(iter(alpha), iter(non_alpha)))


def _merge_streams(a, b):
    streams = [a, b]
    heads = []
    for j, s in enumerate(streams):
        try:
            heads.append((next(s), j))
        except StopIteration:
            pass

    while True:
        heads.sort(reverse=True)
        try:
            (_, c), j = heads.pop()
        except IndexError:
            return
        else:
            yield c
            try:
                heads.append((next(streams[j]), j))
            except StopIteration:
                pass
