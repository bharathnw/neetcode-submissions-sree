class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        dp = [[float("inf")] * (C + 1) for _ in range(R + 1)]

        dp[R-1][C] = 0

        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
        
        return dp[0][0]
             

        

        