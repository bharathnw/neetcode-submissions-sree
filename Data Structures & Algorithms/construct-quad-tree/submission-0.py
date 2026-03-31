"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':


        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break
            if allSame == True:
                return Node(grid[r][c], True)

            m = n//2
            topLeft = dfs(m, r, c)
            topRight = dfs(m, r, c+m)
            bottomLeft = dfs(m, r+m, c)
            bottomRight = dfs(m, r+m, c+m)
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(len(grid), 0, 0)
            