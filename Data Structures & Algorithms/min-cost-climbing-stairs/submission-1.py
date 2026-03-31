class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return -1
        if len(cost) <= 2:
            return min(cost)

        dp = [0] * (len(cost) + 1)
        dp[len(cost)] = cost[-1]
        dp[len(cost)-1] =  cost[-2]
        for i in range(len(dp)-3, -1, -1):
            if i > 0:
                dp[i] = cost[i-1] + min(dp[i+1], dp[i+2])
            else:
                dp[i] = min(dp[i+1], dp[i+2])
        
        return dp[0]
        