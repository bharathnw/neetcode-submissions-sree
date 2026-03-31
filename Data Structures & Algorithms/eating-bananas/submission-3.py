class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        minSpeed = 1
        maxSpeed = max(piles)

        l, r = minSpeed, maxSpeed
        res = 0
        while l <= r:
            actualTime = 0
            m = (l+r)//2
            for pile in piles:
                actualTime += math.ceil(pile/m)
            
            if actualTime <= h:
                res = m
                r = m - 1
            else:
                l = m+1
        return res

            

        