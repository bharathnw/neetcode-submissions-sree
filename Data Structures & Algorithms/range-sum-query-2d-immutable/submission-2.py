class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j > 0:
                    matrix[i][j] += matrix[i][j-1]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0:
                    matrix[i][j] += matrix[i-1][j]
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        currSum = self.matrix[row2][col2]
        
        left = self.matrix[row2][col1-1] if col1 > 0 else 0
        top = self.matrix[row1-1][col2] if row1 > 0 else 0
        topLeft = self.matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return currSum - left - top + topLeft