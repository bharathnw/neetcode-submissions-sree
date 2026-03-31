class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        L, R = 0, 1

        while R < len(prices):
            print(L,R)
            if prices[L] > prices[R]:
                L = R
            profit = prices[R] - prices[L]
            maxProfit = max(maxProfit, profit)
            R += 1
        return maxProfit
        