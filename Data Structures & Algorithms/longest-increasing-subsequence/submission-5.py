class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [-1 for _ in range(len(nums))]

        dp[-1] = 1
        res = 1
        for i in range(len(nums)-2, -1, -1):
            dp[i] = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] =  max(dp[i], 1+dp[j])
            res = max(res, dp[i])

        return res                        
            

            


