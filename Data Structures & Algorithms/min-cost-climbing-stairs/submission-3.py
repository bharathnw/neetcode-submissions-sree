class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {len(cost): 0, len(cost)+1: 0}

        for i in range(len(cost)-1, -1, -1):
            dp[i] = min(dp[i+1]+cost[i], dp[i+2] + cost[i])
        
        return min(dp[0], dp[1])