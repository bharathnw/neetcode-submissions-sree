# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return True, 0
            
            leftB, left = dfs(node.left)
            rightB, right = dfs(node.right)
            isBal = leftB and rightB and abs(left - right) <= 1
            return isBal, 1+max(left, right)
        isB, _ = dfs(root)
        return isB
        