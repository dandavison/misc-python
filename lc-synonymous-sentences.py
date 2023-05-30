# https://leetcode.com/problems/synonymous-sentences


import itertools
from collections import defaultdict
from typing import List


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        edges = make_graph(synonyms)
        synonyms = [get_synonyms(word, edges) for word in text.split()]
        sentences = itertools.product(*synonyms)
        return sorted(" ".join(s) for s in sentences)
        

def make_graph(synonyms):
    edges = defaultdict(set)
    for s, t in synonyms:
        edges[s].add(t)
        edges[t].add(s)
    return dict(edges)


def get_synonyms(word, edges):
    stack, visited = [word], {word}
    while stack:
        w = stack.pop()
        for neighbor in edges.get(w, set()):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return visited
