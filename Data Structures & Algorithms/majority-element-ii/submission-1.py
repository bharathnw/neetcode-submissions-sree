class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)

        x, y = 0, 0
        x_count, y_count = 0, 0

        for num in nums:
            if num == x:
                x_count += 1
            elif num == y:
                y_count += 1
            elif x_count == 0:
                x = num
                x_count += 1
            elif y_count == 0:
                y = num
                y_count += 1
            else:
                x_count -= 1
                y_count -= 1
        
        x_count, y_count = 0, 0
        for num in nums:
            if num == x:
                x_count += 1
            if num == y:
                y_count += 1
        res = []
        if x_count > (n//3):
            res.append(x)
        if y_count > (n//3):
            res.append(y)
        
        return res
        