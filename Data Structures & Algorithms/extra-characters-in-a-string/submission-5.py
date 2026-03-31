class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        cache = {}
        def dfs(i):
            if i >= len(s):
                return 0
            if i in cache:
                return cache[i]
                
            res = float('inf')
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in words:
                    res = min(res, dfs(j+1))
            #skipping 1st character

            res = min(1 + dfs(i+1), res)
            cache[i] = res
            return res
        
        return dfs(0)

            
             

        