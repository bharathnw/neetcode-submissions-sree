class Solution:
    def findMin(self, nums: List[int]) -> int:

        L, R = 0, len(nums)-1
        res = nums[0]

        while L <= R:
            mid = (L+R)//2

            res = min(res, nums[mid])

            if nums[L] <= nums[mid]:
                res = min(res, nums[L])
                L = mid + 1
            else:
                res = min(res, nums[mid])
                R = mid - 1
        return res
        