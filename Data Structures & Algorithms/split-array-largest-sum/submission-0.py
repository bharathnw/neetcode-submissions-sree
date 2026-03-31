class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        l = max(nums)
        r = sum(nums)
        res = 0
        def split_parts(cap):
            parts = 1
            currCap = 0
            minCap = float('-inf')
            for num in nums:
                if currCap+num > cap:
                    parts += 1
                    currCap = 0
                currCap += num
                minCap = max(minCap, currCap)
            return parts, minCap


        while l <= r:
            avg = (l+r)//2
            parts, minCap = split_parts(avg)
            if parts <= k:
                r = avg - 1
                res = minCap
            else:
                l = avg + 1

        return res

        