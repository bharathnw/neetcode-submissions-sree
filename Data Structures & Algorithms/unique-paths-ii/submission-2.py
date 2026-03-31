class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        cache = {}
        def bruteForce(r, c):
            if r == M or c == N or obstacleGrid[r][c] == 1:
                return 0
            if r == M-1 and c == N-1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]
            
            cache[(r,c)] = bruteForce(r+1,c) + bruteForce(r, c+1)
            return cache[(r,c)]
        
        return bruteForce(0,0)
        