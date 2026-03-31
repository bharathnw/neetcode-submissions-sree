class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}

        for tot in range(1, amount+1):
            dp[tot] = amount + 1
            for c in coins:
                if tot - c >= 0:
                    dp[tot] = min(dp[tot], 1 + dp[tot-c])
        
        return dp[amount] if dp[amount] != (amount + 1) else -1



                

            
            
        