class Solution:
    def totalNQueens(self, n: int) -> int:

        col_set = set()
        pos_set = set()
        neg_set = set()

        res = 0

        def backtrack(row):
            nonlocal res
            if row == n:
                res += 1
                return
            
            for c in range(n):
                if c in col_set or (row+c) in pos_set or (row-c) in neg_set:
                    continue
                col_set.add(c)
                pos_set.add(row+c)
                neg_set.add(row-c)
                backtrack(row+1)
                col_set.remove(c)
                pos_set.remove(row+c)
                neg_set.remove(row-c)
        backtrack(0)
        return res

        