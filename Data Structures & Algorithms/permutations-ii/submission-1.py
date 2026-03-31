class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = set()

        cache = [0] * len(nums)

        def backtrack(arr):
            if len(arr) == len(nums):
                res.add(tuple(arr[:]))
                return
            for j in range(len(nums)):
                if cache[j] != 1:
                    cache[j] = 1
                    arr.append(nums[j])
                    backtrack(arr)
                    arr.pop()
                    cache[j] = 0
        
        backtrack([])
        return list(res)
            
        