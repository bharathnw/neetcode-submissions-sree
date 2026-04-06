class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        L = 0
        currSum = 0
        currLen = 10 ** 6
        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                currLen = min(currLen, R-L+1)
                currSum -= nums[L]
                L += 1
        
        return currLen if (currLen != 10**6) else 0

