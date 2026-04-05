class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        dp = [[0] * (C+1) for _ in range(R+1)]

        dp[R-1][C-1] = 1
        
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                dp[r][c] += (dp[r+1][c] + dp[r][c+1])

        return dp[0][0]
