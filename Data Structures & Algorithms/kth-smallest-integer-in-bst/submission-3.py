# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        heap = []
        out = 0
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            heapq.heappush(heap, node.val)
            dfs(node.right)
        dfs(root)
        for i in range(k):
            out = heapq.heappop(heap)
        return out

        