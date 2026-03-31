class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = []

        cache = {}

        def dfs(i, isBuying):
            if (i, isBuying) in cache:
                return cache[(i, isBuying)]

            if i >= len(prices):
                return 0
            
            cool = dfs(i+1, isBuying)

            if isBuying:
                buy = dfs(i+1, False) - prices[i]
                cache[(i,isBuying)] = max(buy, cool)
                return max(buy, cool)
            else:
                sell = dfs(i+2, True) + prices[i]
                cache[(i,isBuying)] = max(sell, cool)
                return max(sell, cool)
        
        return dfs(0, True)