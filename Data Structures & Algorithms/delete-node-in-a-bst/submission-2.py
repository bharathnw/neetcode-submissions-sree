# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findMinNode(node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                return None
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            else:
                minNode = findMinNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root


        