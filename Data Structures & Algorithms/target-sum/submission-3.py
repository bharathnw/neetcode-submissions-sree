class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(index, total):
            if (index, total)  in cache:
                return cache[(index, total)]
            if len(nums) == index:
                if total == target:
                    return 1
                return 0
            add = dfs(index+1, total + nums[index])
            sub = dfs(index+1, total - nums[index])
            cache[(index, total)] = add + sub
            return cache[(index, total)]
        return dfs(0, 0)

