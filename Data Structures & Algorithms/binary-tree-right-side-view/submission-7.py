# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        output = []
        q = collections.deque()
        level = 0
        if root:
            q.append(root)
        while len(q) > 0:
            levelOutput = []
            for i in range(len(q)):
                curr = q.popleft()
                levelOutput.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            output.append(levelOutput[-1])
            level += 1
        return output
        