class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        downSlope = set()
        upSlope = set()
        col = set()

        res = []

        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                path = ["".join(row) for row in board]
                res.append(path)
                return
            for c in range(n):
                if c in col or (c-r) in downSlope or (c+r) in upSlope:
                    continue
                col.add(c)
                downSlope.add(c-r)
                upSlope.add(c+r)
                board[r][c] = "Q"
                dfs(r+1)
                col.remove(c)
                downSlope.remove(c-r)
                upSlope.remove(c+r)
                board[r][c] = "."
        dfs(0)
        return res
        

            