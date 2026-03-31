class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        arr = []
        def backTrack(openCnt, closedCnt):
            if openCnt == n and closedCnt == n:
                res.append("".join(arr[:]))
                return
            
            if openCnt < n:
                arr.append('(')
                backTrack(openCnt+1, closedCnt)
                arr.pop()
            if closedCnt < openCnt:
                arr.append(')')
                backTrack(openCnt, closedCnt+1)
                arr.pop()
        
        backTrack(0,0)
        return res
