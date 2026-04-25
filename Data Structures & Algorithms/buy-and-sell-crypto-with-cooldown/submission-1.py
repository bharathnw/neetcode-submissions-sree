class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, isBuy):
            if i >= len(prices):
                return 0
            if (i, isBuy) in dp:
                return dp[(i, isBuy)]
            res = dfs(i+1, isBuy)

            if isBuy:
                res = max(res, -prices[i] + dfs(i+1, False))
            else:
                res = max(res, prices[i]+dfs(i+2, True))
            dp[(i, isBuy)] = res
            return res
        
        return dfs(0, True)
        