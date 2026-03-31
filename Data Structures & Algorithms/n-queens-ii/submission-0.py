class Solution:
    def totalNQueens(self, n: int) -> int:

        col_set = set()
        pos_set = set()
        neg_set = set()

        def backTrack(row, res):
            if row == n:
                res += 1
                return res
            
            for c in range(n):
                if c in col_set or (row+c) in pos_set or (row-c) in neg_set:
                    continue
                
                col_set.add(c)
                pos_set.add(row+c)
                neg_set.add(row-c)
                res = backTrack(row+1, res)
                col_set.remove(c)
                pos_set.remove(row+c)
                neg_set.remove(row-c)
            return res
        
        return backTrack(0, 0)
