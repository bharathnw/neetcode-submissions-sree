class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            minText = text1
            maxText = text2
        else:
            minText = text2
            maxText = text1
        M = len(minText)
        N = len(maxText)
        dp = [0] * (N+1)

        for i1 in range(1, N + 1):
            curr = [0] * (M+1)
            for i2 in range(1, M+1):
                if maxText[i1-1] == minText[i2-1]:
                    curr[i2] = 1 + dp[i2-1]
                else:
                    curr[i2] = max(dp[i2], curr[i2-1])
            dp = curr 
        return dp[M]


        


            
        