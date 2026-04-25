class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}

        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2)-j
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 1 + dfs(i+1, j+1)

            if word1[i] == word2[j]:
                res = min(res, dfs(i+1, j+1))
            else:
                res = min(res, 1+dfs(i+1, j), 1+dfs(i, j+1))
            dp[(i, j)] = res
            return res
        
        return dfs(0,0)