from collections import deque

def make_node(preorder, inorder):
    # base case
    if not preorder:
        return None

    node_val, *preorder = preorder

    if not preorder:
        return TreeNode(node_val)

    # recursion
    if node_val not in inorder:
        print(node_val, inorder)
        exit()
    left_size = inorder.index(node_val)

    inorder_left, inorder = inorder[:left_size], inorder[left_size:]
    preorder_left, preorder = preorder[:left_size], preorder[left_size:]

    return TreeNode(
        node_val,
        make_node(preorder_left, inorder_left),
        make_node(preorder, inorder)
    )


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        queue = deque([self])
        output = []
        while queue:
            node = queue.popleft()
            output.append(node.val if node else 'null')
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return output

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(make_node(preorder, inorder).serialize())


# preorder = [3,9,5,6,20,15,4,7,8,9]
# inorder = [5,9,6,3,4,15,20,8,7,9]

# print(make_node(preorder, inorder).serialize())


