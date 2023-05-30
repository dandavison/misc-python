from itertools import islice

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie(products)
        # print(f"trie: {trie.trie}")
        suggestions = []
        entered = ""
        for c in searchWord:
            entered += c
            suggestions.append(trie.get_suggestions(entered))

        return suggestions

class Trie:

    def __init__(self, words):
        self.trie = {}
        self.end = "$"
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        # print(f"add: {word}")
        node, rest = self._find_node(word)
        # print(f"node, rest: {node}, {rest}")
        for c in rest:
            # print(f"add: {c} {self.trie}")
            node[c] = {}
            node = node[c]
        node[self.end] = {}

    def _find_node(self, word) -> Tuple[dict, str]:
        node = self.trie
        i = 0
        for c in word:
            # print(f"find: {c}")
            if c not in node:
                break
            else:
                node = node[c]
                i += 1
        return node, word[i:]

    def get_suggestions(self, string) -> List[str]:
        """
        If node is not a prefix of anything in the trie, return [].
        """
        node, rest = self._find_node(string)
        # print(f"found: {node} __{rest}__")
        if rest:
            # Didn't find string; no completions.
            return []
        else:
            # Return 3 best completions (possibly including string itself)
            return list(islice(self.iter_words(node, string), 3))

    def iter_words(self, node, prefix):
        """
        Yield words rooted at node in lexicographic order.
        """
        chars = set(node.keys())
        if self.end in chars:
            yield prefix
            chars.remove(self.end)
        for c in sorted(chars):
            yield from self.iter_words(node[c], prefix=prefix + c)
