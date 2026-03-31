class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0
        visits = set()

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r,c) in visits:
                return 0
            visits.add((r,c))
            area = 1
            for dr, dc in dirs:
                area += dfs(dr+r, dc+c)
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_area = max(dfs(i, j), max_area)

        return max_area
            

            
        