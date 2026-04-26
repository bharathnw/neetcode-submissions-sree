class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total//2

        dp = {}
        

        def dfs(i, tot):
            if (i, tot) in dp:
                return dp[(i, tot)]
            if tot == target:
                return True
            if i == len(nums) or tot > target:
                return False
            dp[(i, tot)] = dfs(i+1, tot+nums[i]) or dfs(i+1, tot)
            return dp[(i, tot)]
            
        
        return dfs(0, 0)