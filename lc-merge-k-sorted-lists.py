# https://leetcode.com/problems/merge-k-sorted-lists/
# # You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Runtime: 208 ms, faster than 18.54% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 23.9 MB, less than 5.03% of Python3 online submissions for Merge k Sorted Lists.

from heapq import heappush, heappop
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return make_linked_list(heapq.merge(*(make_generator(node) for node in lists)))
        

def make_linked_list(generator):
    val = next(generator, None)
    if val is None:
        return None
    else:
        head = curr = ListNode(val=val)

    while True:
        try:
            val = next(generator)
        except StopIteration:
            return head
        else:
            curr.next = ListNode(val=val)
            curr = curr.next


class Solution_2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        generators = [make_generator(node) for node in lists]
        
        heap = []
        for i, g in enumerate(generators):
            try:
                heapq.heappush(heap, (next(g), i))
            except StopIteration:
                pass
            
        head = curr = None
        while heap:
            # Emit the next value from the heap
            val, i = heapq.heappop(heap)
            node = ListNode(val=val, next=None)
            if not curr:
               head = curr = node
            else:
                curr.next = node
                curr = node
            # Push the next value from the stream it came from (if it isn't empty)
            try:
                heapq.heappush(heap, (next(generators[i]), i))
            except StopIteration:
                pass

        return head
        

def make_generator(node):
    while node:
        yield node.val
        node = node.next


class Solution_2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        return make_linked_list(heapq.merge(*map(make_generator, lists)))

    def mergeKLists_1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        lists = [make_generator(l) for l in lists]

        # Initialize: fill heap with heads of all lists
        for i, gen in enumerate(lists):
            _try_move_head_to_heap(gen, i, heap)

        if not heap:
            return None

        out_list_head = None
        while True:
            # Remove the minimum from the heap and emit it into our output list
            try:
                val, i = heappop(heap)
            except IndexError:
                return out_list_head
            else:
                if out_list_head is None:
                    out_list_head = out_list_ptr = ListNode(val)
                else:
                    out_list_ptr.next = ListNode(val)
                    out_list_ptr = out_list_ptr.next
                _try_move_head_to_heap(lists[i], i, heap)


def _try_move_head_to_heap(gen, i, heap):
    try:
        val = next(gen)
    except StopIteration:
        # TODO: should we remove exhausted input lists from further consideration?
        pass
    else:
        heappush(heap, (val, i))
