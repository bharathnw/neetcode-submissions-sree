class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index, total):
            if len(nums) == index:
                if total == target:
                    return 1
                return 0
            add = dfs(index+1, total + nums[index])
            sub = dfs(index+1, total - nums[index])
            return add + sub        
        return dfs(0, 0)

