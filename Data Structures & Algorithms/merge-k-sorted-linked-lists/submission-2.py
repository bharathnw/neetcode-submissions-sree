# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        res = lists[0]

        for i in range(1, len(lists)):
            
            curr = res
            sib = lists[i]

            dummy = node = ListNode(-1)

            while sib and curr:
                if curr.val < sib.val:
                    node.next = curr
                    curr = curr.next
                else:
                    node.next = sib
                    sib = sib.next
                node = node.next
            node.next = sib or curr
            res = dummy.next
        return dummy.next



        