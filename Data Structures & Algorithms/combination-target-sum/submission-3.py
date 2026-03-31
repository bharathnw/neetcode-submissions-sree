class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        arr = []
        def backtrack(tot, index):
            if tot == target:
                res.append(arr[:])
                return
            if tot > target or index == len(nums):
                return 
            arr.append(nums[index])
            backtrack(nums[index] + tot, index)
            arr.pop()
            backtrack(tot, index+1)
        
        backtrack(0, 0)
        return res
                