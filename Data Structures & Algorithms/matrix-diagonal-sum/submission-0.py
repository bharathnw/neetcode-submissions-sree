class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        mapper = set()
        r = len(mat)
        c = len(mat[0])

        tot = 0

        i = 0
        j = 0

        while i < r and j < c:
            mapper.add((i, j))
            tot += mat[i][j]
            i += 1
            j += 1
        
        i = r -1
        j = 0

        while i >= 0 and j < c:
            if (i, j) not in mapper:
                tot += mat[i][j]
            i -= 1
            j += 1
                
        return tot