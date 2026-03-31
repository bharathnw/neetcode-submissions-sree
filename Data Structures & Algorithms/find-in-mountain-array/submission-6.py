class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        cache = {}
        n = mountainArr.length()

        l, r = 0, n-1
        while l < r:
            m = (l+r)//2
            
            left = cache.get(m-1, mountainArr.get(m-1))
            right = cache.get(m+1, mountainArr.get(m+1))
            mid = cache.get(m, mountainArr.get(m))
            
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        
        peak = m
        l, r = 0, peak

        while l <= r:
            m = (l+r)//2
            mid = cache.get(m, mountainArr.get(m))

            if mid < target:
                l = m + 1
            elif mid > target:
                r = m - 1
            else:
                return m
        
        l, r = peak+1, n-1
        while l <= r:
            m = (l+r)//2
            mid = cache.get(m, mountainArr.get(m))
            if mid > target:
                l = m + 1
            elif mid < target:
                r = m - 1
            else:
                return m

        return -1
            
