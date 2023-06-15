"""
cf
https://leetcode.com/problems/lru-cache/
https://leetcode.com/problems/lfu-cache/
"""
from collections import deque
from dataclasses import dataclass


class OrderedDict:
    def __init__(self):
        self._keys = deque()
        self._dict = {}

    def get(self, key):
        return self._dict[key]

    def put(self, key, value):
        self._keys.append(key)
        self._dict[key] = value

    def keys(self):
        return list(self._keys)

    @classmethod
    def fromkeys(cls, keys):
        d = cls()
        for key in keys:
            d.put(key, None)
        return d

    def popitem(self, last=True):
        """
        The popitem() method for ordered dictionaries returns and removes a
        (key, value) pair. The pairs are returned in LIFO order if last is true
        or FIFO order if false.
        """
        if last:
            key = self._keys.pop()
        else:
            key = self._keys.popleft()
        return key, self._dict.pop(key)

    def move_to_end(self, key, last=True):
        """
        Move an existing key to either end of an ordered dictionary. The item is
        moved to the right end if last is true (the default) or to the beginning
        if last is false. Raises KeyError if the key does not exist:
        """
        if last:
            self._keys.append(self._keys.popleft())
        else:
            self._keys.appendleft(self._keys.pop())


def test_popitem_lifo():
    d = OrderedDict.fromkeys("abcde")

    assert d.popitem(last=True) == ("e", None)
    assert d.popitem(last=True) == ("d", None)


def test_popitem_fifo():
    d = OrderedDict.fromkeys("abcde")
    assert d.popitem(last=False) == ("a", None)
    assert d.popitem(last=False) == ("b", None)


def test_move_to_end():
    d = OrderedDict.fromkeys("abcde")
    d.move_to_end("b")
    __import__("pdb").set_trace()
    assert "".join(d.keys()) == "acdeb"

    d.move_to_end("b", last=False)
    assert "".join(d.keys()) == "bacde"


if __name__ == "__main__":
    test_popitem_lifo()
    test_popitem_fifo()
    test_move_to_end()
