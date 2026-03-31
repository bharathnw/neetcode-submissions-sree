class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def searchTarget(l, r):
            m = (l+r)//2
            print(l, m, r)
            if l > m or r < m:
                return m + 1
            if nums[m] == target:
                return m
            if nums[m] > target:
                return searchTarget(l, m-1)
            if nums[m] < target:
                return searchTarget(m+1, r)

        return searchTarget(0, len(nums)-1)        