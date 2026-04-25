# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head

        slow, fast = curr, curr.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        first = curr

        reversed = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = reversed
            reversed = curr
            curr = nxt
        
        while reversed and first:
            f_next, r_next = first.next, reversed.next
            first.next = reversed
            reversed.next = f_next
            first = f_next
            reversed = r_next
        
        
