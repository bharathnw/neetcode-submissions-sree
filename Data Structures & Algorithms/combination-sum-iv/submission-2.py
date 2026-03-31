class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        cache = {}
        def dfs(currSum):
            if currSum == target:
                return 1
            if currSum > target:
                return 0
            if currSum in cache:
                return cache[currSum]
            total = 0
            for i in range(len(nums)):
                total += dfs(currSum+nums[i])
            cache[currSum] = total
            return total
        
        return dfs(0)


                
        