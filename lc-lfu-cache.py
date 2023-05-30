"""
https://leetcode.com/problems/lfu-cache/submissions/

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

- LFUCache(int capacity) Initializes the object with the capacity of the data
  structure.

- int get(int key) Gets the value of the key if the key exists in the cache.
  Otherwise, returns -1.

- void put(int key, int value) Update the value of the key if present, or
  inserts the key if not already present. When the cache reaches its capacity,
  it should invalidate and remove the least frequently used key before inserting
  a new item.

  For this problem, when there is a tie (i.e., two or more keys with the same
  frequency), the least recently used key would be invalidated. To determine the
  least frequently used key, a use counter is maintained for each key in the
  cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to
the put operation). The use counter for a key in the cache is incremented when
either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
"""

from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self._use_counter = OrderedDict()
        self._n_keys = 0

    def get(self, key: int) -> int:
        try:
            val = self._cache[key]
            self._use_counter[key] += 1
            return val
        except KeyError:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if self._capacity:
            if key not in self._cache:
                if self._n_keys == self._capacity:
                    self._expire_one_key()
                self._n_keys += 1
            self._cache[key] = value
            self._use_counter[key] += 1
            
    def _expire_one_key(self):
        # TODO: break ties on recency
        lfu_key, _ = min(self._use_counter.items(), key=lambda item: item[1])
        del self._cache[lfu_key]
        self._n_keys -= 1
        del self._use_counter[lfu_key]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
