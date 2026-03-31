class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            if target == 0:
                return 2
            else:
                return 0

        dp = [defaultdict(int) for _ in range(len(nums))]
        dp[0][nums[0]] = 1
        dp[0][-nums[0]] = 1 + dp[0].get(-nums[0], 0)

        for i in range(1, len(nums)):
            for total, count in dp[i-1].items():
                dp[i][total + nums[i]] += count
                dp[i][total - nums[i]] += count
            
        return dp[len(nums)-1][target]

