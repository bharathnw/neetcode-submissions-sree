# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def mergeTwo(h1, h2):
            tail = curr = ListNode()
            while h1 and h2:
                h1N = h1.next
                h2N = h2.next

                if h1.val < h2.val:
                    curr.next = h1
                    h1 = h1N
                else:
                    curr.next = h2
                    h2 = h2N
                curr = curr.next
            
            if h1:
                curr.next = h1
            if h2:
                curr.next = h2
            
            return tail.next

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None

                merged.append(mergeTwo(l1, l2))
            
            lists = merged
        
        return lists[0]

        

                

                

        