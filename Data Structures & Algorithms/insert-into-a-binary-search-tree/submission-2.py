# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        curr = root
        prev = None

        if not root:
            return TreeNode(val)


        while curr:
            if curr.val < val:
                prev = curr
                curr = curr.right
            else:
                prev = curr
                curr = curr.left
        if prev.val < val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root
        