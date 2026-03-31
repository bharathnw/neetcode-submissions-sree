class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M = len(word1)
        N = len(word2)
        dp = [[0] * (N+1) for _ in range(M+1)]

        for i in range(M+1):
            dp[i][0] = i
        for j in range(N+1):
            dp[0][j] = j
        res = 0
        
        for i1 in range(1,M+1):
            for i2 in range(1, N+1):
                
                if word1[i1-1] == word2[i2-1]:
                    dp[i1][i2] = dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = 1 + min(dp[i1][i2-1], dp[i1-1][i2], dp[i1-1][i2-1])
        return dp[M][N]



        