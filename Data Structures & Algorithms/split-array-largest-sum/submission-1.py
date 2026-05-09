class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l = max(nums)
        r = sum(nums)

        res = float('inf')

        def findSets(tot):
            parts = 1
            currSum = 0

            for num in nums:
                if (currSum + num) > tot:
                    currSum = 0
                    parts += 1
                currSum += num
            return parts

        while l <= r:

            avgTot = (l+r)//2

            totSets = findSets(avgTot)

            if totSets <= k:
                res = avgTot
                r = avgTot - 1
            else:
                l = avgTot + 1
        
        return res

        