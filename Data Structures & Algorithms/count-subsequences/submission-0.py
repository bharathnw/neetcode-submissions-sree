class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        res = [0]

        def dfs(i, r):
            if r == len(t):
                res[0] += 1
                return
            if i == len(s):
                return
            if s[i] == t[r]:
                dfs(i+1, r+1)
                dfs(i+1, r)
            else:
                dfs(i+1, r)
        dfs(0,0)
        return res[0]
            