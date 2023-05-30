# https://leetcode.com/problems/remove-nth-node-from-end-of-list


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We must traverse the list once to reach the end: O(K)
        # Having reached the end (position K-1) we must unlink the node with position K-1-n.
        # To do so, we require references to nodes K-1-(n+1) and K-1-(n-1).

        nodes = []
        ptr = head
        i = 0
        while True:
            nodes.append(ptr)
            i += 1
            ptr = ptr.next
            if not ptr:
                break

        if i - (n + 1) >= 0:
            left = nodes[i - (n + 1)]
        else:
            left = None

        if i - (n - 1) < len(nodes):
            right = nodes[i - (n - 1)]
        else:
            right = None

        if left is None:
            head = right
        else:
            left.next = right

        return head
