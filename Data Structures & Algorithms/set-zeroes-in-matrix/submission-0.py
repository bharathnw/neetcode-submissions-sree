class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])
        x_set = set()
        y_set = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    x_set.add(r)
                    y_set.add(c)
        
        for r in range(rows):
            for c in range(cols):
                if r in x_set or c in y_set:
                    matrix[r][c] = 0
