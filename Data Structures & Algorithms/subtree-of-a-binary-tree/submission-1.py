# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(tree, subTree):
            if not tree and not subTree:
                return True
            elif not tree and subTree:
                return False
            elif tree and not subTree:
                return False
            elif tree.val != subTree.val:
                return False
            return isSameTree(tree.left, subTree.left) and isSameTree(tree.right, subTree.right)
      
        if not root:
            return False

        if isSameTree(root,subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    




        