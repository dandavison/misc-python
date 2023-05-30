# Write a function that, given a string, determines if it's a concatenation of two dictionary words
from typing import List, Optional


# Worst-case O(n chars in words)
def is_concat(s: str, words: List[str]) -> bool:
    word_set = set(words)
    for word in words:  # O(n words)
        suffix = get_suffix(word, s)  # O(n chars in word)
        if suffix is not None and suffix in word_set:
            return True
    return False


def get_suffix(prefix: str, string: str) -> Optional[str]:
    before, _, after = string.partition(prefix)
    return after if not before else None


# Alternatively, we could build a trie of words [ O(n chars in words) ]
# and use the trie

import random
from string import ascii_lowercase


def random_string(n: int):
    "".join(random.choice(ascii_lowercase) for _ in range(n))


def find_key():
    key = random_string(1000)
    for i in range(100):
        my_set = {"a", "b"}
        if key in my_set:
            return True
    return False


if __name__ == "__main__":
    words = ["a", "b", "ab"]
    assert is_concat("aa", words)
    assert is_concat("ab", words)
    assert is_concat("aab", words)
    assert is_concat("bab", words)
    assert is_concat("abb", words)
    assert not is_concat("ac", words)
    assert not is_concat("abaa", words)
