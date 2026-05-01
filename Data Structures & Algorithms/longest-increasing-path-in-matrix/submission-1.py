class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = {}
        R, C = len(matrix), len(matrix[0])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)] 
            res = 1
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if nr == R or nc == C or nr < 0 or nc < 0 or matrix[r][c] >= matrix[nr][nc]:
                    continue
                res = max(res, 1+dfs(nr, nc))
            dp[(r,c)] = res
            return res
        
        res = 0
        for i in range(R):
            for j in range(C):
                res = max(res, dfs(i, j))
        
        return res
        
                    
            
        