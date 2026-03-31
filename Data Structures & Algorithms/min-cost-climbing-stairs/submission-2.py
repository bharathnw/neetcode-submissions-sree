class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            c = cost[i]
            res = min(c + dfs(i+1), c + dfs(i+2))
            dp[i] = res
            return res
        
        return min(dfs(0), dfs(1))