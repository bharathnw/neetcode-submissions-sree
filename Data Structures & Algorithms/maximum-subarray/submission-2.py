class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        currSum = 0
        maxSum = nums[0]

        for num in nums:
            currSum = max(currSum, 0)
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum

        
        