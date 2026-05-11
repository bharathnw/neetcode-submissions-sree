class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(isBuy, i):
            if (isBuy, i) in cache:
                return cache[(isBuy, i)]
            if i == len(prices):
                return 0
            
            res = dfs(isBuy, i+1)
            
            if isBuy:
                res = max(prices[i] + dfs(False, i+1), res)
            else:
                res = max(-prices[i] + dfs(True, i+1), res)
            cache[(isBuy, i)] = res
            return res
        
        return dfs(False, 0)

            
        