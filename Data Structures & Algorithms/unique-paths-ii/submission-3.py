class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        dp = [[0] * (N + 1)] * (M + 1)


        dp[M-1][N-1] = 1
        
        for r in range(M-1, -1, -1):
            for c in range(N-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]