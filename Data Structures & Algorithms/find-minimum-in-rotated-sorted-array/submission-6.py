class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        if len(nums) == 1:
            return nums[0]

        if nums[L] < nums[R]:
            return nums[L]

        while L < R:
            mid = (L+R)//2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        
        return nums[L]

        

