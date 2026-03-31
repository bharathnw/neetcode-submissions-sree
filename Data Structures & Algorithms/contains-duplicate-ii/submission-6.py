class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        cache = set()
        for R in range(len(nums)):
            if (R - L) > k:
                cache.remove(nums[L])
                L += 1
            if nums[R] in cache:
                return True
            cache.add(nums[R])

        return False 