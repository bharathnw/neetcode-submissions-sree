class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        max_res = nums[0]
        res = nums[0]

        curr = nums[0]

        for num in nums[1:]:
            print(num, curr)
            if num > curr:
                res += num
            else:
                res = num
            max_res = max(res, max_res)
            curr = num
        
        return max_res
        



