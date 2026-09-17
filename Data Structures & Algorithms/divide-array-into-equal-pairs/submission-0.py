class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        

        num_set = {}

        for num in nums:
            if num in num_set:
                num_set[num] += 1
            else:
                num_set[num] = 1
        

        for item in num_set.values():
            if item % 2 == 1:
                return False
            
        return True