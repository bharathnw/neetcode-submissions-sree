import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        output = r

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for ele in piles:
                hours += math.ceil(ele/mid)
            if hours <= h:
                r = mid - 1
                output = mid
            else: 
                l = mid + 1
        return output