# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = deque()
        res = []
        if not root:
            return []
        q.append(root)
        while q:
            length = len(q)
            
            for index in range(length):
                curr = q.popleft()
                if index == length - 1:
                    res.append(curr.val)
                if not curr:
                    continue
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res    
            

        