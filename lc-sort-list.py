# https://leetcode.com/problems/sort-list


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = list(make_generator(head))
        # array.sort()
        array = quicksort(array)
        return make_linked_list(array)


def make_linked_list(array):
    if not array:
        return None
    head = ptr = ListNode(array[0])
    for el in array[1:]:
        ptr.next = ListNode(el)
        ptr = ptr.next
    return head


def make_generator(head):
    while head:
        yield head.val
        head = head.next


def quicksort(array):
    if not array:
        return array
    else:
        midpoint = len(array) // 2
        left = []
        right = []
        for i, el in enumerate(array):
            if i != midpoint:
                if el < array[midpoint]:
                    left.append(el)
                else:
                    right.append(el)
        return quicksort(left) + [array[midpoint]] + quicksort(right)


print(quicksort([1]))
print(quicksort([2, 1, 3]))
