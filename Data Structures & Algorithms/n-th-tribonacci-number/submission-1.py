class Solution:
    def tribonacci(self, n: int) -> int:
        
        cache = {}
        def calculate(n):
            if n in cache:
                return cache[n]
            if n <= 0:
                return 0
            if n <= 2:
                return 1
            cache[n] = calculate(n-1) + calculate(n-2) + calculate(n-3)
            return cache[n]
        return calculate(n)
            
        