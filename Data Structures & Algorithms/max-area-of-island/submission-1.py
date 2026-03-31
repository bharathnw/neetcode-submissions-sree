class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        areaList = []
        directions = [[1,0],[-1,0], [0,1], [0,-1]]
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
               area += dfs(r+dr, c+dc)
        
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    print(area)
                    areaList.append(area)
                    area = 0
        if len(areaList) == 0:
            return 0
        else:
            return max(areaList)