# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        levels = defaultdict(list)
        res = []

        def dfs(node, level):
            if not node:
                return 
            levels[level].append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        dfs(root, 0)
        
        for i in range(len(levels.keys())):
            res.append(levels[i][0])
        return res
        

        