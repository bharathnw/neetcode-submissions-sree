class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = [0]
        def dfs(index, total):
            if len(nums) == index:
                if total == target:
                    res[0] += 1
                return
            dfs(index+1, total + nums[index])
            dfs(index+1, total - nums[index])
        
        dfs(0, 0)
        return res[0]

