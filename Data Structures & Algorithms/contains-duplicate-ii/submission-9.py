class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window_set = set()
        L = 0
        for R in range(len(nums)):
            if (R - L) <= k:
                if nums[R] in window_set:
                    return True
            else:
                window_set.remove(nums[L])
                L += 1
                if nums[R] in window_set:
                    return True
            window_set.add(nums[R])
        
        return False


        