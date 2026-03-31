class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        if nums[L] < nums[R]:
            return nums[L]

        while L <= R:
            if nums[L] > nums[R]:
                R -= 1
            else:
                return nums[R+1]
        

