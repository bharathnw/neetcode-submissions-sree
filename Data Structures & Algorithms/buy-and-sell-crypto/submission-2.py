class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        
        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                pr = prices[R] - prices[L]
                profit = max(pr, profit)
        return profit


            

            