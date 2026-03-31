class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        kmap = {}
        for num in nums:
            if num in kmap:
                return True
            else:
                kmap[num] = 1
        return False

        