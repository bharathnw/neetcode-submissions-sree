class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(tot):
            if tot > target:
                return 0
            if tot == target:
                return 1
            if tot in cache:
                return cache[tot]
            res = 0

            for j in range(len(nums)):
                res += dfs(tot + nums[j])
            cache[tot] = res
            return res
        
        return dfs(0)
            
        