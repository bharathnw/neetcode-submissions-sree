class Solution:
    def checkValidString(self, s: str) -> bool:

        dp = {}

        def dfs(leftCt, rightCt, i):
            if (leftCt, rightCt, i) in dp:
                return dp[(leftCt, rightCt, i)]
            if leftCt < rightCt:
                return False
            if i == len(s):
                return leftCt == rightCt
            
            if s[i] == '(':
                dp[(leftCt, rightCt, i)] = dfs(leftCt+1, rightCt, i+1)
                return dp[(leftCt, rightCt, i)]
            elif s[i] == ')':
                dp[(leftCt, rightCt, i)] = dfs(leftCt, rightCt+1, i+1)
                return dp[(leftCt, rightCt, i)]
            
            dp[(leftCt, rightCt, i)] = dfs(leftCt+1, rightCt, i+1) or dfs(leftCt, rightCt+1, i+1) or dfs(leftCt, rightCt, i+1)
            return dp[(leftCt, rightCt, i)]
        
        return dfs(0,0, 0)
        

        