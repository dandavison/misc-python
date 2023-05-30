# https://leetcode.com/problems/design-add-and-search-words-data-structure


class WordDictionary:
    def __init__(self):
        self.terminal = "$"
        self.trie = {self.terminal: {}}

    def addWord(self, word: str) -> None:
        ptr = self.trie
        for c in word:
            ptr = ptr.setdefault(c, {})
        ptr[self.terminal] = {}

    def search(self, word: str) -> bool:
        return self._search(list(word), self.trie)

    def _search(self, word, trie):
        if not word:
            return self.terminal in trie
        c, *word = word
        if c == ".":
            for d, subtrie in trie.items():
                if d != self.terminal:
                    if self._search(word, subtrie):
                        return True
        elif c in trie:
            return self._search(word, trie[c])

        return False
