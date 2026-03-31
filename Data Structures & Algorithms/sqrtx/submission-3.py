class Solution:
    def mySqrt(self, x: int) -> int:

        isNeg = False

        if x < 0:
            x = x * -1
            isNeg = True
        
        l, r = 1, x
        res = 0

        while l <= r:
            m = (l+r)//2
            
            if m * m < x:
                l = m+1
                res = m
            elif m * m > x:
                r = m-1
            else:
                return m
        
        return res

        