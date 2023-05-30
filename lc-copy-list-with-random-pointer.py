"""
# https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the
original list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random
--> Y, then for the corresponding two nodes x and y in the copied list, x.random
--> y.

Return the head of the copied linked list.
"""

from collections import defaultdict

class Solution_1:
    # Not mine!
    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution
    def copyRandomList(self, head: "Node") -> "Node":
        dic = collections.defaultdict(lambda: Node(0))
        dic[None] = None
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]

class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None

        old_head = head
        new_head = Node(x=old_head.val)

        old_random_nodes = [old_head.random]
        old_node_to_new_node = {old_head: new_head}
        
        # Deep copy
        new_node = new_head
        for old_node in iter_nodes(old_head.next):
            old_random_nodes.append(old_node.random)
            new_node.next = Node(x=old_node.val)
            new_node = new_node.next           
            old_node_to_new_node[old_node] = new_node

        # Set random pointers
        for new_node, old_random_node in zip(iter_nodes(new_head), old_random_nodes):
            if old_random_node:
                new_node.random = old_node_to_new_node[old_random_node]
            else:
                new_node.random = None
            
        return new_head
    
    
def iter_nodes(head):
    if head:
        yield head
        yield from iter_nodes(head.next)

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
