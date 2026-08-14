class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs(left, right, val):
            if left == n and right == n:
                res.append(val)
                return res
            
            if right > left or left > n:
                return
            
            dfs(left+1, right, val+'(')
            dfs(left, right+1, val+')')
            
        dfs(0,0,'')
        return res
