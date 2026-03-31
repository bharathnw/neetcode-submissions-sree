class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        R = len(nums)
        L = 0

        while L < R:
            if nums[L] == val:
                R -= 1
                nums[L] = nums[R]
            else:
                L += 1  
        return L
        