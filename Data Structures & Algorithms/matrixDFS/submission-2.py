class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        def dfs(grids, r, c, used):
            if r < 0 or c < 0  or r == rows or c == cols or (r, c) in used or grids[r][c] == 1:
                return 0
            if r == rows-1 and c == cols-1:
                return 1
            used.add((r,c))
            count = 0
            count += dfs(grids, r+1, c, used)
            count += dfs(grids, r-1, c, used)
            count += dfs(grids, r, c+1, used)
            count += dfs(grids, r, c-1, used)

            used.remove((r,c))
            return count
        
        return dfs(grid, 0, 0, set())


        