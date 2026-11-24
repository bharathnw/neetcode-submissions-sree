class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        out = 0

        if not mat:
            return out
        
        sets = set()

        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    out += mat[i][j]
                    sets.add((i, j))
        
        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat)):
                if i == (len(mat) - j - 1) and (i, j) not in sets:
                    out += mat[i][j]
        
        return out
