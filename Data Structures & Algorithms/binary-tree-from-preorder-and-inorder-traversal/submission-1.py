# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.pre_index = 0  # pointer for preorder list

        def helper(inorder_part):
            if not inorder_part:
                return None

            # Root from preorder index
            root_val = preorder[self.pre_index]
            root = TreeNode(root_val)
            print(root_val, "from Preorder")  # for debug

            self.pre_index += 1  # move to next preorder value

            mid = inorder_part.index(root_val)
            root.left = helper(inorder_part[:mid])
            root.right = helper(inorder_part[mid+1:])
            return root

        return helper(inorder)
