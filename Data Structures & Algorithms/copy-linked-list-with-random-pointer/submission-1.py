"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head
        cache = {}
        while curr:
            if curr not in cache:
                cache[curr] = Node(curr.val)
            curr = curr.next    
        
        dummy = Node(0)
        curr = dummy
        def dfs(node, du):
            if not node:
                return
            du.next = cache[node]
            if node.random in cache:
                du.next.random = cache[node.random]
            dfs(node.next, du.next)
        dfs(head, dummy)
        return curr.next
            

        