class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
    
        currMin = 0
        currMax = 0
        globalMin = float('inf')
        globalMax = float('-inf')

        for num in nums:
            currMin = min(num+currMin, num)
            currMax = max(num+currMax, num)
            globalMin = min(currMin, globalMin)
            globalMax = max(currMax, globalMax)
        if globalMax < 0:
            return globalMax
        return max(globalMax, sum(nums) - globalMin)