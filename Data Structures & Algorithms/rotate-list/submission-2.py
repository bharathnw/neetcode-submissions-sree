# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
            
        curr = head
        dummy = ListNode()
        dummy.next = head
        i = 0
        node_map = {}

        while curr:
            node_map[i] = curr
            curr = curr.next
            i += 1
        
        n = len(node_map)
        k = k % n

        if k == 0:
            return head

        curr = dummy

        r = node_map[n - k - 1]

        r_h = r.next
        r.next = None
        h = curr.next
        tail = node_map[n-1]
        curr.next = r_h
        tail.next = h

        return dummy.next


        

        