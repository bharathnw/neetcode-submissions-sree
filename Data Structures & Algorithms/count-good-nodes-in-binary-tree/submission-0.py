# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        target = root.val
        res = [0]

        def dfs(node, target):
            if not node:
                return 
            if node.val >= target:
                res[0] += 1
                target = node.val
            dfs(node.left, target)
            dfs(node.right, target)
        dfs(root, target)
        return res[0]



        