import pdb


def solution(h, q):
    n_nodes = sum(2**level for level in range(h))
    vals = range(1, n_nodes + 1)
    root = make_tree(vals)
    root.relabel(iter(vals))
    assert root
    output = []
    for val in q:
        output.append(root.find_parent(val))
    return output


def make_tree(vals):
    if not vals:
        return None
    mid = len(vals) // 2
    root = Node(vals[mid])
    root.left = make_tree(vals[:mid])
    root.right = make_tree(vals[mid+1:])
    return root


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(%s, left=%s, right=%s)" % (self.val, self.left, self.right)

    def relabel(self, labels):
        if self.left:
            self.left.relabel(labels)
        if self.right:
            self.right.relabel(labels)
        self.val = next(labels)

    def find_parent(self, val, parent=-1):
        if val == self.val:
            return parent
        return (self.left and self.left.find_parent(val, parent=self.val) or
                self.right and self.right.find_parent(val, parent=self.val))


# print(solution(3, [1, 4, 7]))