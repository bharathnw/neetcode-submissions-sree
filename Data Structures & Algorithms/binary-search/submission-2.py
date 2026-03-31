class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        return self.searchHelper(nums, target, L, R)

    def searchHelper(self, nums, target, L, R):
        mid = (L + R) // 2
        print(L, R, mid)
        if target == nums[mid]:
            return mid
        if L > mid or R < mid:
            return -1
        
        if target < nums[mid]:
            return self.searchHelper(nums, target, L, (mid-1))
        if target > nums[mid]:
            return self.searchHelper(nums, target, mid+1, R)
        


        