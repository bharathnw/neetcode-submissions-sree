class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, currSum):
            if (i, currSum) in dp:
                return dp[(i, currSum)]

            if currSum == target and i == len(nums):
                return 1
            
            if i == len(nums):
                return 0
            
            res = dfs(i+1, currSum + nums[i]) + dfs(i+1, currSum - nums[i])
            dp[(i, currSum)] = res
            return dp[(i, currSum)]
        
        return dfs(0, 0)
        