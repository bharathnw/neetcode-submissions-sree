class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = nums[:]
    
        for i in range(len(nums)-3, -1, -1):
            dp[i] = max(nums[i]+ dp[i+2], dp[i+1])
        
        return dp[0]
        