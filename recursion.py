"""Make linter error go away."""


def sumr(n):
    """
    Return the sum of the integers 1, ..., n.

    >>> sumr(4)
    10
    """
    # Return n + < sum of integers 1 to n-1 >
    if n == 0:
        return 0
    return n + sumr(n - 1)


def factorial(n):
    """
    Return the product of the integers 1, ..., n.

    >>> factorial(4)
    24
    """
    # Return n * <product of integers 1 to n - 1>
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_palindrome(s):
    """
    Return True iff s is a palindrome.

    >>> is_palindrome('hannah')
    True
    >>> is_palindrome('henna')
    False
    """
    # if (first and last are same) return is_palindrome(middle)
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1 : len(s) - 1])
    else:
        return False


def fibonacci(n):
    """
    Return nth fibonacci number.

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def flatten(l):
    """
    l is a list of lists, with arbitrary nesting.

    Return a flat list containing the contents.

    >>> flatten([[5], 17, [[3, [40]]]])
    [5, 17, 3, 40]
    """
    # children of root node are
    # [5]                         [5]
    # 17                          [17]
    # [[3, [40]]]                 [3, 40]

    # for each child, flatten it
    # concatenate those flat results

    def is_flat(el):
        if isinstance(el, list):
            return False
        return True

    if is_flat(l):
        return [l]

    flat = []
    for el in l:
        flat.extend(flatten(el))
    return flat


def powerset(s):
    """
    Return the set containing all subsets of s.
    """
    pass


def cartesian_product(list_of_lists):
    """
    Return the Cartesian product of the lists contained in `list_of_lists`.

    The Cartesian product of `list_of_lists` is defined to be:

    <DEFINITION>
    """


def _merge_sorted_arrays(x, y, reverse=True):
    assert reverse

    if not x:
        return y
    elif not y:
        return x
    elif x[0] > y[0]:
        return [x[0]] + _merge_sorted_arrays(x[1:], y)
    else:
        return [y[0]] + _merge_sorted_arrays(x, y[1:])


class Node:
    """Eff off linter."""

    def __init__(self, key, value=None, left=None, right=None):
        """Pls."""
        self.key = key  # type: integer
        self.value = value  # type: anything
        self.left = left  # type: Node
        self.right = right  # type: Node


def sum_binary_tree(node):
    """
    Each node of the binary tree holds a key and value, as well as left/right
    pointers.

    Return the sum of the keys.
    """
    # return (
    #     root key + sum_binary_tree(root.left) + sum_binary_tree(root.right))
    if node is None:
        return 0
    return node.key + sum_binary_tree(node.left) + sum_binary_tree(node.right)


def print_binary_tree(node):
    """
    Each node of the binary tree holds a key and value, as well as left/right
    pointers.

    Print out the keys in order.
    """
    # print_binary_tree(root.left)
    # print root
    # print_binary_tree(root.right)
    if node is None:
        return
    print_binary_tree(node.left)
    print(node.key)
    print_binary_tree(node.right)


def no_elevens(n):
    """
    Return all length-n sequences of 6s and 1s that have no adjacent 1s.

    Return value is a list of lists.

    >>> no_elevens(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    """
    # return a list containing [6] + <the subsequent lists of n-1 6s and 1s
    # that don't contain >1 1>, + [1] + <subsequent lists of n-1 6s and 1s
    # that don't contain >1 1> ... except they can't start with 1!
    # so in fact
    # [1,6] + <subsequent lists of n-2 6s and 1s that don't contain >1 1>
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6], [1]]
    a, b = no_elevens(n - 1), no_elevens(n - 2)
    return [[6] + s for s in a] + [[1, 6] + s for s in b]


# TODO
def sixty_ones(link):
    """
    Return the number of times 6,1 occurs in the linked list.
    """
    # return the sum of the times i'th element of a linked list == 6 followed
    # by i'th element.next == 1
    if link.is_empty or link.next is None:
        return 0
    elif link.next == 6 and link.next.next == 1:
        return 1 + sixty_ones(link.next.next)
    return sixty_ones(link.next)


# TODO
def towers_of_hanoi(n):
    # return a sequence of moves to get a subtower (1 disk) to the finish,
    # then a second subtower to the finish, for n subtowers
    pass


if __name__ == "__main__":
    tree = Node(20)
    tree.left = Node(10)
    tree.right = Node(30)

    tree.left.left = Node(5)
    tree.left.right = Node(15)
    tree.right.left = Node(25)

    print_binary_tree(tree)
    print("\n")
    print(sum_binary_tree(tree))
