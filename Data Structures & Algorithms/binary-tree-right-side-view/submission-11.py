# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = {}

        if not root:
            return []

        def dfs(level, node):
            if not node:
                return
            if level not in levels:
                levels[level] = node.val
            dfs(level+1, node.right)
            dfs(level+1, node.left)

        dfs(0, root)
        res = []
        for i in range(len(levels)):
            res.append(levels[i])
        
        return res