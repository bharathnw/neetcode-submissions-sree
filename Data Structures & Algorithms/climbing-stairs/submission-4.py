class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def count(cnt):
            if cnt < 0:
                return 0
            if cnt in cache:
                return cache[cnt]
            if cnt == 0:
                return 1
            cache[cnt] = count(cnt - 1) + count(cnt - 2)
            return cache[cnt]
        
        return count(n)
            



        