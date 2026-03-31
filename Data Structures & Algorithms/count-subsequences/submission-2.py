class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache = {}
        def dfs(i, r):
            if (i, r) in cache:
                return cache[(i,r)]
            if r == len(t):
                return 1
            if i == len(s):
                return 0
            res = 0
            if s[i] == t[r]:
                res += (dfs(i+1, r+1) + dfs(i+1, r))
            else:
                res += (dfs(i+1, r))
            cache[(i,r)] = res
            return res
        
        return dfs(0,0)
            