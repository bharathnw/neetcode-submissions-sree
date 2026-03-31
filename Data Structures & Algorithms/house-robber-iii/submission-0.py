# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        cache = {}

        def getProfit(node):
            if not node:
                return 0
            if node in cache:
                return cache[node]
            cache[node] = node.val
            if node.left:
                cache[node] += (getProfit(node.left.left) + getProfit(node.left.right))
            
            if node.right:
                cache[node] += (getProfit(node.right.left) + getProfit(node.right.right))

            cache[node] = max(cache[node], getProfit(node.left) + getProfit(node.right))
            return cache[node]
        
        return getProfit(root)
            
            
        