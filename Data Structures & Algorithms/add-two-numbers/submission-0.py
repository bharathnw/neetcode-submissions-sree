# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverseList(l):
            curr = l
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        strl1, strl2 = "", ""
        rl1 = reverseList(l1)
        rl2 = reverseList(l2)

        while rl1:
            strl1 += str(rl1.val)
            rl1 = rl1.next

        while rl2:
            strl2 += str(rl2.val)
            rl2 = rl2.next

        outstr = reversed(str(int(strl1) + int(strl2)))
        
        h = newHead = ListNode()
        for ch in outstr:
            h.next = ListNode(int(ch))
            h = h.next
        return newHead.next



            

        