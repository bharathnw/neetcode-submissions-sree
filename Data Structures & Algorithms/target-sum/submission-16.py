class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, tot):
            if (i, tot) in dp:
                return dp[(i, tot)]
            if i == len(nums) and tot == target:
                return 1
            if i == len(nums):
                return 0
                
            res = 0
            res += dfs(i+1, tot+nums[i])
            res += dfs(i+1, tot-nums[i])
            dp[(i, tot)] = res
            return res

        return dfs(0,0)
        