class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3

        for num in nums:
            counter[num] += 1
        
        index, curr = 0, 0

        while index < len(nums):

            while counter[curr] == 0:
                curr += 1
            
            nums[index] = curr
            counter[curr] -= 1
            index += 1
        
        return nums
        
        