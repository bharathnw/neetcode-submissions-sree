class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_buy = prices[0]

        for price in prices:
            if price < min_buy:
                min_buy = price
            else:
                profit = price-min_buy
                max_profit = max(max_profit, profit)

        return max_profit





        '''
        for price in prices:
            if buy < price:
                profit = price - min_buy
                min_buy = price
                total_profit += profit
            else:
                min_buy = price
            print (price, min_buy, total_profit)
        return total_profit

        '''