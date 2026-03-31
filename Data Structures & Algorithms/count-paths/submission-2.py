class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visits = set()
        
        def backtrack(r, c):
            if r < 0  or c < 0 or r == m or c == n or (r, c) in visits:
                return 0
            if r == m-1 and c == n-1:
                return 1
            
            res = 0
            for dr, dc in [(1, 0), (0, 1)]:
                visits.add((r, c))
                res += backtrack(dr+r, dc+c)
                visits.remove((r, c))
            return res
        
        return backtrack(0, 0)

        
                
            
