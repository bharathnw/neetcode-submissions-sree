class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = float('inf')
        L = 0
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]

            while curr_sum >= target:
                curr_sum -= nums[L]
                res = min(res, R-L+1)
                L += 1
        return res if res != float('inf') else 0
            
        