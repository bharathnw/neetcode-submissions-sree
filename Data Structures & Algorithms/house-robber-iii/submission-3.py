# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        curr = root

        cache = {None: 0}
        def dfs(node):
            if node in cache:
                return cache[node]
            
            res = node.val
            if node.left:
                res += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                res += dfs(node.right.left) + dfs(node.right.right)
            
            cache[node] = max(res, dfs(node.left) + dfs(node.right))
            return cache[node]
    

        return dfs(root)

        