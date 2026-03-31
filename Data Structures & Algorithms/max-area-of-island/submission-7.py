class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visits = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r == R or c == C or grid[r][c] == 0 or (r, c) in visits: 
                return 0
            visits.add((r, c))
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            res = 1
            for dr, dc in dirs:
                res += dfs(dr+r, dc+c)
            
            return res

        area = 0
        for i in range(R):
            for j in range(C):
                if (i, j) not in visits:
                    area = max(dfs(i, j), area)
        
        return area
                    
                


        