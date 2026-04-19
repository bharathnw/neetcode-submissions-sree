class Solution:
    def checkValidString(self, s: str) -> bool:

        dp = {}

        def dfs(leftCt, i):
            if (leftCt, i) in dp:
                return dp[(leftCt, i)]
            if leftCt < 0:
                return False
            if i == len(s):
                return leftCt == 0
            
            if s[i] == '(':
                dp[(leftCt, i)] = dfs(leftCt+1, i+1)
                return dp[(leftCt, i)]
            elif s[i] == ')':
                dp[(leftCt, i)] = dfs(leftCt-1, i+1)
                return dp[(leftCt, i)]
            
            dp[(leftCt, i)] = dfs(leftCt+1, i+1) or dfs(leftCt-1, i+1) or dfs(leftCt, i+1)
            return dp[(leftCt, i)]
        
        return dfs(0,0)
        

        