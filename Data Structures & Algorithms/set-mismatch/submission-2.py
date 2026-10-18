class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        num_set = {}

        for num in nums:
            num_set[num] = num_set.get(num, 0) + 1

        res = []
        missing = None
        for num in range(1, len(nums)+1):
            if num in num_set and num_set[num] > 1:
                res.append(num)
            elif num not in num_set:
                missing = num
        if missing is not None:
            res.append(missing)
        return res




