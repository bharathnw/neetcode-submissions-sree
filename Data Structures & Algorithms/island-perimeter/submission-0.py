class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visits = set()

        def dfs(r, c):
            if (r, c) in visits:
                return 0
            if  r < 0 or c < 0 or r == R or c == C or grid[r][c] == 0:
                return 1
            visits.add((r,c))
            res = 0 
            res += dfs(r+1, c)
            res += dfs(r-1, c)
            res += dfs(r, c+1)
            res += dfs(r, c-1)
            return res
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]== 1:
                    return dfs(i, j)
        return 0
        