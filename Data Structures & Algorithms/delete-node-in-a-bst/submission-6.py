# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def getMax(node):
            if node.right:
                return getMax(node.right)
            else:
                return node

        
        def search(node, key):
            if not node:
                return
            
            if node.val > key:
                node.left = search(node.left, key)
            elif node.val < key:
                node.right = search(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                maxNode = getMax(node.left)
                node.val = maxNode.val
                node.left = search(node.left, node.val)
            return node

        return search(root, key)
