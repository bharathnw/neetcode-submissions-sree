class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        dp = {}
        def calMax(i, j):

            if i > j :
                return 0

            if (i, j) in dp:
                return dp[(i, j)]
            
            maxProfit = 0

            for k in range(i, j+1):
                profit = nums[i-1] * nums[k] * nums[j+1]
                profit += calMax(i, k-1) + calMax(k+1, j)
                maxProfit = max(maxProfit, profit)
            dp[(i, j)] = maxProfit
            return maxProfit
        
        return calMax(1, len(nums)-2)

                


            
            
        