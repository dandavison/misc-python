# https://leetcode.com/problems/substring-with-concatenation-of-all-words


import itertools
from collections import Counter, deque

# passes all tests

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target_char_counts = Counter(itertools.chain.from_iterable(words))
        window_size = sum(target_char_counts.values())
        
        
        window = deque()
        window_char_counts = Counter()

        stream = enumerate(s)
        
        indices = []
        for i, c in stream:
            window.append(c)
            window_char_counts[c] += 1
            if i >= window_size:
                exited = window.popleft()
                assert window_char_counts[exited]
                window_char_counts[exited] -= 1
                if not window_char_counts[exited]:
                    del window_char_counts[exited]
            # print(list(window), window_char_counts)
            if window_char_counts == target_char_counts:
                window_start = i - window_size + 1
                # print("\n", i, window_start)
                if matches("".join(window), words):
                    indices.append(window_start)
                    
        return indices
    

def matches(window: str, words: List[str]) -> bool:
    n = len(words[0])
    words = Counter(words)
    i = 0
    for _ in range(sum(words.values())):
        s = window[i: i + n]
        # print(s, words)
        if words[s]:
            words[s] -= 1
            i += n
        else:
            # print(window, "does not match")
            return False

    # print(window, "matches")
    return True
