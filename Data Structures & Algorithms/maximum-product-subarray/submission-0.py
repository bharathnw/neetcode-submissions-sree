class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = nums[0]

        for num in nums:
            temp = currMax * num
            currMax = max(num*currMax, num*currMin, num)
            currMin = min(temp, currMax, num, currMin * num)
            res = max(currMax, res)
        
        return res