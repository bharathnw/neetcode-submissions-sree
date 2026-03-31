class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]

        currSum = 0
        res = nums[0]

        for num in nums:
            currSum = max(currSum, 0)
            currSum += num
            res = max(currSum, res)
        return res






        