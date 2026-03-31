class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        out = []

        def dfs(i, t):
            if t == target:
                out.append(res[:])
                return
            if i >= len(nums) or t > target:
                return
            res.append(nums[i])
            dfs(i, t + nums[i])
            res.pop()
            dfs(i+1, t)
        dfs(0,0)
        return out

        