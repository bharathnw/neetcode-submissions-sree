class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        res = float('inf')

        l = max(weights)
        r = sum(weights)

        def calDays(cap):
            weight = 0
            daysCt = 1
            for num in weights:
                if weight + num > cap:
                    weight = 0
                    daysCt += 1
                weight += num
            return daysCt
        
        while l <= r:
            cap = (l+r)//2
            daysCt = calDays(cap)
            if daysCt <= days:
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res

        