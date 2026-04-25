class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0
            
            res = 0

            for j in range(min(i+2, len(s))):
                word = s[i:j+1]
                if len(word) == 1 or (len(word) > 1 and int(word) <= 26):
                    res += dfs(j+1)
            dp[i] = res
            return res
        
        return dfs(0)