# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        # q = deque([])

        # res = []

        # q.append([root])

        # while q:
        #     item = q.popleft()
        #     stepVals = []
        #     next_items = []
        #     for element in item:
        #         stepVals.append(element.val)
        #         if element.left:
        #             next_items.append(element.left)
        #         if element.right:
        #             next_items.append(element.right)
                
        #     if next_items:
        #         q.append(next_items)
        #     res.append(stepVals)
        # return res

        res_map = defaultdict(list)

        def dfs(level, node):
            if not node:
                return 
            res_map[level].append(node.val)
            if node.left:
                dfs(level+1, node.left)
            if node.right:
                dfs(level+1, node.right)
            
        
        dfs(0, root)
        res = []
        for item in res_map.keys():
            res.append(res_map[item])
        
        return res
        
            


















