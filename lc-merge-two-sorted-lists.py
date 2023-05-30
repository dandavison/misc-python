"""
https://leetcode.com/problems/merge-two-sorted-lists/submissions/

Merge two sorted linked lists and return it as a sorted list. The list should be
made by splicing together the nodes of the first two lists.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l2.val < l1.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l2, l1.next)
            return l1
