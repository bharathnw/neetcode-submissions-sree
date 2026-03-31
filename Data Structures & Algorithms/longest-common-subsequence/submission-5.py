class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        M = len(text1)
        N = len(text2)

        dp = [[0] * (N+1) for _ in range(M+1)]

        for i1 in range(1, M+1):
            for i2 in range(1, N+1):
                if text1[i1-1] == text2[i2-1]:
                    dp[i1][i2] = 1 + dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])
        return dp[M][N]


        


            
        