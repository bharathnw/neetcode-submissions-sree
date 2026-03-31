# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        q = deque()

        q.append(root)
        level = 0
        while q:
            level += 1
            for i in range(len(q)):
                item = q.popleft()
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
        return level
        