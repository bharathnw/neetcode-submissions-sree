class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dp = [False] * len(nums)

        dp[len(nums)-1] = True

        for i in range(len(nums)-1,-1,-1):
            for num in range(nums[i],-1,-1):
                if num + i >= len(nums) or dp[num+i] == True:
                    dp[i] = True
                    break
        
        return dp[0]
        