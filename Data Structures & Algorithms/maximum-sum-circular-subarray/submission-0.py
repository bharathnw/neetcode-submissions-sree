class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        currMax = 0
        currMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        total = 0
        for num in nums:
            total += num
            currMax = max(currMax, 0)
            currMin = min(currMin, 0)
            currMax += num
            currMin += num
            maxSum = max(currMax, maxSum)
            minSum = min(currMin, minSum)
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
        