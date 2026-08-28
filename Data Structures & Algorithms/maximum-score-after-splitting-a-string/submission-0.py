class Solution:
    def maxScore(self, s: str) -> int:
        
        self.max_score = 0

        def dfs(i):

            if i == len(s):
                return
            
            left = s[:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            self.max_score = max(self.max_score, score)

            dfs(i+1)
        
        dfs(1)
        return self.max_score
            
