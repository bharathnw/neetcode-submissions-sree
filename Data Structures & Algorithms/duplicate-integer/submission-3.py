class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = []
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.append(num)
        
        return False