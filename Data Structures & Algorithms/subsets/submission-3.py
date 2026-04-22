class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        arr = []

        def dfs(i):
            if i == len(nums):
                res.append(arr[:])
                return 
            arr.append(nums[i])
            dfs(i+1)
            arr.pop()
            dfs(i+1)
        
        dfs(0)
        return res
        