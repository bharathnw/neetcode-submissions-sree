class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        visits = set()
        def dfs(r, c):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] == 0:
                return 1
            if (r, c) in visits:
                return 0
            visits.add((r, c))
            return dfs(r + 1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(r, c)
        
        return 0

         
        