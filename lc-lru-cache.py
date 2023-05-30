"""
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

- int get(int key) Return the value of the key if the key exists, otherwise
  return -1.

- void put(int key, int value) Update the value of the key if the key exists.
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""
from collections import OrderedDict
from typing import Dict, Optional


class LRUCache_LeetCodeSolution(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity

        self._dict: Dict[int, _ListNode] = {}
        self._front_sentinel = _ListNode()
        self._end_sentinel = _ListNode()
        self._front_sentinel.next = self._end_sentinel
        self._end_sentinel.prev = self._front_sentinel

    def get(self, key: int) -> int:
        try:
            node = self._dict[key]
        except KeyError:
            return -1
        else:
            self._move_to_end(node)
            assert node.value is not None
            return node.value

    def put(self, key: int, value: int) -> None:
        try:
            node = self._dict[key]            
        except KeyError:
            # inserting new key
            if len(self._dict) == self._capacity:
                self._expire_one_key()               
            node = _ListNode(key=key, value=value)    
            self._dict[key] = node
            self._link(self._end_sentinel.prev, node, self._end_sentinel)
        else:
            # updating existing key
            node.value = value
            self._move_to_end(node)

    def _move_to_end(self, node):
        self._unlink(node)
        self._link(self._end_sentinel.prev, node, self._end_sentinel)

    def _expire_one_key(self):
        node_to_expire = self._front_sentinel.next
        if not node_to_expire:
            return
        self._unlink(node_to_expire)
        del self._dict[node_to_expire.key]

    def _unlink(self, node):
        if node in [self._front_sentinel, self._end_sentinel]:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
    def _link(self, prev, node, next):
        if prev:
            prev.next = node
        if next:
            next.prev = node
        node.prev, node.next = prev, next


class _ListNode:
    def __init__(self, prev=None, key=-1, value=-1, next=None):
        self.prev = prev
        self.key = key
        self.value = value
        self.next = next

if __name__ == "__main__":
    ops = [
        "LRUCache",
        "put",
        "put",
        "put",
        "put",
        "get",
        "get",
        "get",
        "get",
        "put",
        "get",
        "get",
        "get",
        "get",
        "get",
    ]
    args = [
        [3],
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4],
        [4],
        [3],
        [2],
        [1],
        [5, 5],
        [1],
        [2],
        [3],
        [4],
        [5],
    ]
    expected = iter([None, None, None, None, None, 4, 3, 2, -1, None, -1, 2, 3, -1, 5])
    cache = LRUCache(0)
    for (op, args) in zip(ops, args):
        if op == "LRUCache":
            cache = LRUCache(*args)
            [capacity] = args
            print(f"capacity: {capacity}\n")
            next(expected)
        else:
            print(op, args)
            output = getattr(cache, op)(*args)
            print("expected", next(expected), "got", output)
            print()


# capacity: 2

# put [1, 1]
# None None

# put [2, 2]
# None None

# get [1]
# 1 1

# put [3, 3]
# expired 1   keys = [2,3]
# None None

# get [2]     ! why is 2 not present?
# -1 2

# put [4, 4]
# expired 2
# None None

# get [1]
# -1 -1

# get [3]
# 3 3

# get [4]
# 4 4
