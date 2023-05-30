def match(pattern: str, string: str) -> int:
    """
    >>> match("", "")
    0
    >>> match("a", "a")
    0
    >>> match("a", "b")
    -1
    >>> match("a", "ba")
    1
    >>> match("ab", "ba")
    -1
    >>> match("a?b", "ba")
    0
    """
    if not pattern:
        return 0
    for i in range(len(string)):
        if _is_match(pattern, string[i:]):
            return i
    return -1


def _is_match(pattern: str, string: str) -> bool:
    if not pattern:
        return not string
    c = pattern[0]
    if c == "*":
        return _is_match(pattern[1:], string[1:])
    elif c == "?":
        return _is_match(pattern[1:], string)
    elif string and c == string[0]:
        return _is_match(pattern[1:], string[1:])
    else:
        return False
