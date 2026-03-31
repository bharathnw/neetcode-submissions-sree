class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        #updating nums, removing wastage
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums)+2
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val-1] = -1 * nums[val-1]
        
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                return i
        
        return len(nums) + 1
                


