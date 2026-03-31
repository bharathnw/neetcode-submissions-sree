# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head
        h = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse = None
        while slow:
            nxt = slow.next
            slow.next = reverse
            reverse = slow
            slow = nxt

        while reverse:
            nxt = h.next
            rnxt = reverse.next
            h.next = reverse
            reverse.next = nxt
            reverse = rnxt
            h = nxt
        if h:
            h.next = None
        








