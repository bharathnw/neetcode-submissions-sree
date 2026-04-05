class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {len(nums)-1 : 0}
        
        for i in range(len(nums)-2, -1, -1):
            res = float('inf')
            for j in range(1, nums[i]+1):
                if (i + j) >= len(nums):
                    res = min(res, 1 + dp[len(nums)-1])
                    continue
                res = min(res, 1 + dp[i+j])
            dp[i] = res
        
        return dp[0]
            
        