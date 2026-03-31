# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        i = 0
        while curr:
            curr = curr.next
            i += 1  

        last = i - n
        i = 0
        dummy = ListNode(0, head)
        curr = dummy
        
        while curr:
            if i == last:
                curr.next = None if not curr.next else curr.next.next
                break
            curr = curr.next
            i += 1

        return dummy.next



