# https://leetcode.com/problems/implement-trie-prefix-tree


# implement-trie-prefix-tree
#
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.terminal = "$"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.trie
        for c in word:
            ptr = ptr.setdefault(c, {})
        ptr[self.terminal] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        result = self._search(word)
        return result is not None and self.terminal in result

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        result = self._search(prefix)
        return result is not None

    def _search(self, string):
        ptr = self.trie
        for c in string:
            try:
                ptr = ptr[c]
            except KeyError:
                return None
        return ptr



sentinel = None

class Trie2:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[sentinel] = sentinel

    def search(self, word: str) -> bool:
        node = self._find_prefix_node(word)
        return node is not None and sentinel in node

    def startsWith(self, prefix: str) -> bool:
        return self._find_prefix_node(prefix) is not None

    def _find_prefix_node(self, word: str) -> Optional[dict]:
        node = self.trie
        for c in word:
            if c not in node:
                return None
            else:
                node = node[c]
        return node
