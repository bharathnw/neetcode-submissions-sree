# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        i = 0
        while curr:
            leftPrev = None
            while i < left:
                leftPrev = curr
                curr = curr.next
                i += 1
            
            L = curr
            while i < right:
                curr = curr.next
                i += 1
            prev = curr.next
            curr.next = None
            curr = L
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            leftPrev.next = prev
            break

        return dummy.next

            
            


        