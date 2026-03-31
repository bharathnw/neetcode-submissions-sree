# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        reversedMid = None
        while mid:
            nxt = mid.next
            mid.next = reversedMid
            reversedMid = mid
            mid = nxt
        
        curr = head
        while reversedMid:
            nxt = reversedMid.next
            currNext = curr.next 
            curr.next = reversedMid
            reversedMid.next = currNext
            reversedMid = nxt
            curr = currNext
        

