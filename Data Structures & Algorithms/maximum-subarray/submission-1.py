class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1
        maxSum = nums[0]
        curr = 0
        for num in nums:
            if curr<0:
                curr = 0
            curr += num
            if curr > maxSum:
                maxSum = curr
        return maxSum
        