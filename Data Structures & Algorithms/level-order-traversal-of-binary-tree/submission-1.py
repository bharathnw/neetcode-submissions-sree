# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        q = deque()
        q.append(root)

        while q:
            level = []
            l = len(q)
            for _ in range(l):
                curr = q.popleft()
                if not curr:
                    continue
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                level.append(curr.val)
            
            if len(level) > 0:
                res.append(level)
        
        return res
        