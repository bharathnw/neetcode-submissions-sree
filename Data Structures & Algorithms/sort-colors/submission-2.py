class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        index = 0
        for i in range(3):
            while i in counter and counter[i] > 0:
                nums[index] = i
                index += 1
                counter[i] -= 1
        return nums

        