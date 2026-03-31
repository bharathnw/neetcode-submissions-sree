class Solution:
    def rob(self, nums: List[int]) -> int:
        preMap = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in preMap:
                return preMap[i]
            preMap[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return preMap[i]
        return dfs(0)

        