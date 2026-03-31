class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res, currSum = 0, 0

        preMap = {0:1}

        for num in nums:
            currSum += num
            diff = currSum - k
            res += 0 if diff not in preMap else preMap[diff]
            if currSum in preMap:
                preMap[currSum] += 1
            else:
                preMap[currSum] = 1
        return res

            

            
        