"""
https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

A Binary Matrix is a matrix in which all the elements are either 0 or 1.

Given quadTree1 and quadTree2. quadTree1 represents a n * n binary matrix and
quadTree2 represents another n * n binary matrix. 

Return a Quad-Tree representing the n * n binary matrix which is the result of
logical bitwise OR of the two binary matrixes represented by quadTree1 and
quadTree2.

Notice that you can assign the value of a node to True or False when isLeaf is
False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly
four children. Besides, each node has two attributes:

- val: True if the node represents a grid of 1's or False if the node represents a
grid of 0's.

- isLeaf: True if the node is leaf node on the tree or False if the
node has the four children.
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        else:
            # Neither is a leaf        
            node = Node(
                val=None,
                isLeaf=None,
                topLeft=self.intersect(quadTree1.topLeft, quadTree2.topLeft),
                topRight=self.intersect(quadTree1.topRight, quadTree2.topRight),
                bottomLeft=self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
                bottomRight=self.intersect(quadTree1.bottomRight, quadTree2.bottomRight),
            )
            vals = set()
            isLeaf = True
            qt1 = node.topLeft
            for qt2 in [node.topRight, node.bottomLeft, node.bottomRight]:
                if qt2.isLeaf:
                    vals.add(qt2.val)
                else:
                    isLeaf = False
                    break
            if isLeaf and len(vals) == 1:
                node.isLeaf = True
                [node.val] = vals
                node.topLeft = node.topRight = node.bottomLeft = node.bottomRight = None
            else:
                node.isLeaf = False
                node.val = False
            return node

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
