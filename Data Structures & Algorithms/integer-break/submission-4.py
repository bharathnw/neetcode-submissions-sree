class Solution:
    def integerBreak(self, n: int) -> int:

        dp = {}

        def findMax(sub):
            if sub <= 2:
                return 1
            if sub in dp:
                return dp[sub]
            res = 0
            for i in range(1,sub):
                rem = sub - i

                res = max(i * rem, res, i * findMax(rem))
            dp[sub] = res
            return res
        
        return findMax(n)

                
                
        