class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        y = set()
        up_slope = set()
        down_slope = set()
        board = [['.'] * n for i in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in y or (r+c) in down_slope or (c-r) in up_slope:
                    continue
                y.add(c)
                up_slope.add(c-r)
                down_slope.add(r+c)
                board[r][c] = 'Q'
                backtrack(r+1)
                y.remove(c)
                up_slope.remove(c-r)
                down_slope.remove(r+c)
                board[r][c] = '.'
        backtrack(0)
        return res


        