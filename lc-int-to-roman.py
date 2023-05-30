# https://leetcode.com/problems/int-to-roman


"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

4   -> IIII -> IV
6   -> VI
8   -> VIII
9   -> VIIII -> IX
14   -> XIIII
15   -> XV
16   -> XVI
18   -> XVIII
19   -> XVIIII  -> XIX
1994 -> MDXXXXIIII -> MCMXCIV
"""
from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        # convert naively
        roman = _convert_naively(num)

        # substitute
        roman = _substitute(roman)

        return "".join(roman)


def _convert_naively(num: int) -> List[str]:
    symbols = [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
    ]
    roman = []
    for symb, val in reversed(symbols):
        div, num = divmod(num, val)
        roman.extend([symb] * div)
    return roman


def _substitute(roman: List[str]) -> List[str]:
    if not roman:
        return roman
    roman = reversed(roman)
    state = next(roman)
    substituted = []
    count = 1
    for symb in roman:
        if symb != state:
            print(f"state = {state}, symb = {symb}, count = {count}")
            if state == "I":
                substituted.append("IX" if symb == "V" else "IV")
            elif state == "X":
                substituted.append("XC" if symb == "L" else "XL")
            elif state == "C":
                substituted.append("CM" if symb == "D" else "CD")
            else:
                substituted.extend([state] * count)
            count = 1
            state = symb
        else:
            last = symb
            count += 1
    substituted.extend([last] * count)
    return list(reversed(substituted))


def _(val):
    print(val)
    return val


if __name__ == "__main__":
    # print(_convert_naively(19))
    print(_substitute(_(_convert_naively(1994))))
