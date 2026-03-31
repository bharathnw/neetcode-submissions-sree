class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = (len(t) + 1) * [0]
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            curr = [0] * (len(t) + 1) 
            for j in range(len(t), -1, -1):
                if j < len(t) and s[i] == t[j]:
                    curr[j] = dp[j+1] + dp[j] 
                else:
                    curr[j] = dp[j]
            dp = curr[:]

        print(dp)
        
        return dp[0]
            