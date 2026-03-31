class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        res = []

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for i in range(COLS):
            sub = []
            for j in range(ROWS):
                sub.append(matrix[j][i])
            res.append(sub)
    
        return res