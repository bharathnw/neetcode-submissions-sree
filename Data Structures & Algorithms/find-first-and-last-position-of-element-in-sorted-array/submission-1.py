class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        l, r = 0, len(nums)-1

        min_i = -1
        max_i = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                min_i = mid
                r = mid - 1
            
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

                min_i = -1
            
        if min_i < 0:
            return [-1,-1]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                max_i = mid
                l = mid + 1
            
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return [min_i, max_i]