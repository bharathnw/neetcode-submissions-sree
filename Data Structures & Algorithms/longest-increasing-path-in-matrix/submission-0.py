class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        self.out = [0]
        cache = {}

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = 1
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = dr+r
                y = dc+c
                if x < 0 or y < 0 or x == m or y == n:
                    continue
                if matrix[x][y] > matrix[r][c]:
                    res = max(res, 1 + dfs(x, y))
            
            cache[(r,c)] = res
            self.out[0] = max(self.out[0], res)
            return res

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        
        return self.out[0]