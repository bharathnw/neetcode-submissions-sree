# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcp(a, b):
            while b !=0:
                a, b = b, a%b
            
            return a

        res = head
        curr = head
        while curr and curr.next:
            nxt = curr.next
            val = gcp(curr.val, nxt.val)
            node = ListNode(val)
            curr.next = node
            node.next = nxt
            curr = nxt
        
        return res



        
        