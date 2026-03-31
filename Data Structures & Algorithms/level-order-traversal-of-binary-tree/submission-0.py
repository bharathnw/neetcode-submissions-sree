
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
            
        q = collections.deque()

        if root:
            q.append(root)

        while len(q) > 0:
            levelVal = []
            for i in range(len(q)):
                curr = q.popleft()
                levelVal.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            output.append(levelVal)
        return output