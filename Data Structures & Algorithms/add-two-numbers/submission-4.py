# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)

        head = dummy

        carry = 0

        while l1 and l2:
            h1 = l1.val
            h2 = l2.val
            val = h1 + h2 + carry
            carry = val//10
            res = val % 10
            head.next = ListNode(res)
            head = head.next
            l1 = l1.next
            l2 = l2.next



        while l1:
            val = carry+l1.val
            carry = val//10
            res = val % 10
            head.next = ListNode(res)
            head = head.next
            l1 = l1.next
        while l2:
            val = carry+l2.val
            carry = val//10
            res = val % 10
            head.next = ListNode(res)
            head = head.next
            l2 = l2.next

        if carry > 0:
            head.next = ListNode(carry)

        return dummy.next    