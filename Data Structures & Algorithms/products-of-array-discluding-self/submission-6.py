class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
                suffix[len(nums)-1-i] = nums[len(nums)-i-1]
            else:
                prefix[i] =  prefix[i-1] * nums[i]
                suffix[len(nums) -1-i] = suffix[len(nums) - i] * nums[len(nums)-1-i]
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[1])
            elif i == len(nums)-1:
                res.append(prefix[-2])
            else:
                res.append(prefix[i-1] * suffix[i+1])
        return res
                