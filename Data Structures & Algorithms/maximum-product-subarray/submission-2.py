class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        


        res, currMax, currMin = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            max_v, min_v = currMax, currMin

            currMax = max(max_v*num, min_v*num, num)
            currMin = min(max_v*num, min_v*num, num)

            res = max(res, currMax)
        
        return res
            