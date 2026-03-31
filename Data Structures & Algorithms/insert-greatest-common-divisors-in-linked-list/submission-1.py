# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a, b):
            while b != 0:
                b, a = a%b, b
            
            return a
        
        curr = head

        while curr and curr.next:
            nxt = curr.next
            val = gcd(curr.val, nxt.val)
            node = ListNode(val, nxt)
            curr.next = node
            curr = nxt
        
        return head
        