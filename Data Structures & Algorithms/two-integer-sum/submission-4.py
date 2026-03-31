class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        num_set[nums[0]] = 0
        for i in range(1,len(nums)):
            if target - nums[i] in num_set:
                return [num_set[target - nums[i]], i]
            num_set[nums[i]] = i
        return []


        