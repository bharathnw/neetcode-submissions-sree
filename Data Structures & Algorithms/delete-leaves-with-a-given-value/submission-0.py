# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        

        curr = root
        prev = None

        def dfs(node, prev):
            if not node:
                return None

            node.left = dfs(node.left, node)
            node.right = dfs(node.right, node)

            
            if not node.left and not node.right and target == node.val:
                return None

            return node

        return dfs(curr, prev)

            

