# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Let's maintain two pointers: One in the position before n (we'll rewire the next) and the other pointer to find the end
        dummy = ListNode(0, head)
        l = dummy
        r = head

        # Create a gap of n nodes
        for _ in range(n):
            r = r.next

        # Move both until r passes the end
        while r:
            l = l.next
            r = r.next

        # l is immediately before the node being removed
        l.next = l.next.next

        return dummy.next