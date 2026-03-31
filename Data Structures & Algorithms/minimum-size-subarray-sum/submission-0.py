class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L, R = 0, 0
        curr_sum = 0
        minNumber = float('inf')
        while R < len(nums):
            curr_sum += nums[R]
            while curr_sum >= target:
                minNumber = min(R-L+1, minNumber)
                curr_sum -= nums[L]
                L += 1
            R += 1
        return 0 if minNumber == float('inf') else minNumber
        