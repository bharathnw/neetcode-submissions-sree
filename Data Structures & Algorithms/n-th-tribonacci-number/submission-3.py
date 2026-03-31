class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}

        def helper(n):
            if n in cache:
                return cache[n]
            if n <= 0:
                return 0
            if n == 1 or n == 2:
                return 1
            cache[n] = helper(n-3) + helper(n-2) + helper(n-1)
            return cache[n] 
        
        return helper(n)
        