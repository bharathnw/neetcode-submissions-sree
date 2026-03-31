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

        def isSame(x1, x2, y1, y2):
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if grid[x1][y1] != grid[i][j]:
                       return False
            return True
        
        def helper(x1, x2, y1, y2):
            if x1 == x2 == y1 == y2:
                return Node(grid[x1][y1], True)
            if isSame(x1, x2, y1, y2) == True:
                return Node(grid[x1][y1], True)
            
            midX = (x1 + x2) // 2
            midY = (y1 + y2) // 2

            topLeft = helper(x1, midX, y1, midY)
            topRight = helper(x1, midX, midY + 1, y2)
            bottomLeft = helper(midX + 1, x2, y1, midY)
            bottomRight = helper(midX + 1, x2, midY + 1, y2)
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        return helper(0, len(grid)-1, 0, len(grid)-1)



        