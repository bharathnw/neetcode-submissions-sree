class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #target is h, min = 1, max = max value of piles
        import math
        left , right = 1, max(piles)

        while left <= right:
            speed = left + ((right - left)//2)
            time = 0
            for pile in piles:
                time = time + math.ceil(pile/speed)
            if time <= h:
                right = speed-1
            elif time >h:
                left = speed+1
            
        return left