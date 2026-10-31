class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        mid = sum(nums)//2

        if sum(nums) % 2 != 0:
            return False
        
        dp = {}

        def dfs(i, tot):
            if (i, tot) in dp:
                return dp[(i, tot)]

            if i == len(nums):
                return mid == tot
            
            dp[(i, tot)] = dfs(i+1, tot+nums[i]) or dfs(i+1, tot)
            return dp[(i, tot)]

        return dfs(0, 0)

