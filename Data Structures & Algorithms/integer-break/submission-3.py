class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}

        def dfs(num):
            if num == 1:
                return num
            if num in cache:
                return cache[num]
            res = 0
            for k in range(1, num):
                right = max((num-k), dfs(num-k))
                left = max(k, dfs(k))
                res = max(res, left*right)
            cache[num] = res 
            return res
        return dfs(n)




