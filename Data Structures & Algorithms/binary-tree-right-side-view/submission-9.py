# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        if not root:
            return []

        q = deque()
        res = [root.val]
        q.append(root)

        while len(q) > 0:

            for i in range(len(q)):
                rm = q.popleft()
                if rm.left:
                    q.append(rm.left)
                if rm.right:
                    q.append(rm.right)
            if len(q) > 0:
                res.append(q[-1].val)
        return res
        