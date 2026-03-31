class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        globalMinSum = float('inf')
        globalMaxSum = float('-inf')
        currMin = 0
        currMax = 0
        for num in nums:
            currMin = min(currMin+num, num)
            currMax = max(currMax+num, num)

            globalMaxSum = max(globalMaxSum, currMax)
            globalMinSum = min(globalMinSum, currMin)
        
        if globalMaxSum < 0:
            return globalMaxSum
        
        return max(globalMaxSum, sum(nums)-globalMinSum)
        