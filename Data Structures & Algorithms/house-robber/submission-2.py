class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        prePrev = nums[0]
        prev = max(prePrev, nums[1])
        for i in range(2,len(nums)):
            temp = prev
            prev = max(nums[i] + prePrev, prev)
            prePrev = temp
        return prev
            



        