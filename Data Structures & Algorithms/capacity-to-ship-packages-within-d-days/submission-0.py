class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def findDays(capacity):
            currCapacity = 0
            daysCnt = 1
            for weight in weights:
                if currCapacity + weight > capacity:
                    daysCnt += 1
                    currCapacity = 0
                currCapacity += weight
            return daysCnt
        
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            capacity = (l+r)//2

            daysCnt = findDays(capacity)

            if daysCnt > days:
                l = capacity + 1
            elif daysCnt <= days:
                r = capacity - 1
                res = min(res, capacity)
            
        return res






        