# https://leetcode.com/problems/design-hashmap


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 2 ** 5
        self.data = [[] for _ in range(self.n)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.n
        self.data[idx] = [(key, value)] + [(k, v) for k, v in self.data[idx] if k != key]
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.n
        return next((v for k, v in self.data[idx] if k == key), -1)
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.n
        self.data[idx] = [(k, v) for k, v in self.data[idx] if k != key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)