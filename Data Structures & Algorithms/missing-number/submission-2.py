class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        currTot = sum(num for num in nums)
        tot = sum(num for num in range(len(nums)+1))
        return tot-currTot