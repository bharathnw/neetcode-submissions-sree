class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        res = []

        def dfs(i):
            if i == len(nums):
                out.append(res[:])
                return
            res.append(nums[i])
            dfs(i+1)
            res.pop()
            dfs(i+1)
        
        dfs(0)
        return out

        