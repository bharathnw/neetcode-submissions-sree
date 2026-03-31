class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}

        def dfs(num):
            if num == 0:
                return 0
            if num in cache:
                return cache[num]
            res = num
            for i in range(1, num):
                if num - (i*i) < 0:
                    continue
                res = min(res, 1 + dfs(num - (i*i)))
            cache[num] = res
            return res
        
        return dfs(n)
        