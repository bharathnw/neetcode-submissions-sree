class Solution:
    def mySqrt(self, x: int) -> int:

        def findSqrt(l, r):
            m = (l+r)//2
            if m*m == x:
                return m
            if l > m or r < m:
                return m
            if m*m > x:
                return findSqrt(l, m-1)
            if m*m < x:
                return findSqrt(m+1, r)
        
        return findSqrt(1, x)
            
    
        