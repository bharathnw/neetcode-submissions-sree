class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        arr = []
        res = []

        def dfs(leftCnt, rightCnt):
            if leftCnt == rightCnt == n:
                res.append("".join(arr))
                return
            if leftCnt < rightCnt or leftCnt > n:
                return 

            arr.append('(')
            dfs(leftCnt+1, rightCnt)
            arr.pop()
            arr.append(')')
            dfs(leftCnt, rightCnt+1)
            arr.pop()
        dfs(0,0)
        return res
        