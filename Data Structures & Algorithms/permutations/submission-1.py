class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        visits = [0 for _ in range(len(nums))]

        def backtrack(i, arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return 
            
            for j in range(len(nums)):
                if visits[j] == 0:
                    visits[j] = 1
                    arr.append(nums[j])
                    backtrack(j+1, arr)
                    arr.pop()
                    visits[j] = 0
        
        backtrack(0,[])
        return res
