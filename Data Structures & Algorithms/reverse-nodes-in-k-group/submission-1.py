# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        
        prev = dummy
        i = 0 
        while True:
            kth_node = prev
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next
            curr = prev.next
            for _ in range(k-1):
                nxt = curr.next
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
            prev = curr
        
        return dummy.next
        

