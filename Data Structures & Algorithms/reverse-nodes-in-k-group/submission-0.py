# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseList(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        def getKthNode(node):
            i = 1
            curr = node
            while i < k and curr:
                curr = curr.next
                i += 1 
            return curr

        curr = head
        kthPrev = None
        while curr:
            kthNode = getKthNode(curr)
            if not kthNode:
                if kthPrev:
                    kthPrev.next = curr
                break

            kthNext = kthNode.next
            kthNode.next = None
            reversedHead = reverseList(curr)
            if curr == head:
                head = kthNode
            else:
                kthPrev.next = kthNode
            
            kthPrev = curr
            curr = kthNext
        
        return head       



            


            


        