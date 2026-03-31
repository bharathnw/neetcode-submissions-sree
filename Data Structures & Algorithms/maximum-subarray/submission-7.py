class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currSum = 0
        res = 0

        for num in nums:
            currSum += num
            if currSum < 0:
                currSum = 0
            res = max(res, currSum)
        
        return res if res > 0 else max(nums)
        