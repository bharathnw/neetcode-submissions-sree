"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        q = deque()
        q.append(root)

        while q:
            level_size = len(q)

            for i in range(level_size):

                item = q.popleft()

                if i < level_size -1:
                    item.next = q[0]
                else:
                    item.next = None
                
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            
        return root
                
        