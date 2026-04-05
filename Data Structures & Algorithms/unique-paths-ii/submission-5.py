class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])
        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            if r == R or c == C or obstacleGrid[r][c] == 1:
                return 0
            if r == R-1 and c == C-1:
                return 1
            
            dp[(r,c)] = dfs(r+1, c) + dfs(r, c+1)
            return dp[(r, c)]
        
        return dfs(0, 0)
