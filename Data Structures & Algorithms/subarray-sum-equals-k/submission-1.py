class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cache = {0:1}
        if not nums:
            return -1

        res = 0
        L = 0
        currSum = 0
        for R in range(len(nums)):
            currSum += nums[R]
            res += cache.get(currSum-k, 0) 
            cache[currSum] = cache.get(currSum, 0) + 1
        return res