class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        res = [0]
        def dfs(i, tot):
            if i == len(nums) and tot == target:
                res[0] += 1
                return
            if i == len(nums):
                return
            
            dfs(i+1, tot+nums[i])
            dfs(i+1, tot-nums[i])
        
        dfs(0, 0)

        return res[0]
        