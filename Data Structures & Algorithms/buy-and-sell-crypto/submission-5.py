class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        curr = prices[0]
        for price in prices[1:]:
            if price < curr:
                curr = price
                continue
            res = max(res, price-curr)
        
        return res
