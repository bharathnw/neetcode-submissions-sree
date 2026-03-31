class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        T = 0
        B = len(matrix)-1
        L = 0
        R = len(matrix[0]) -1

        while T <= B:
            TM = (T + B)//2
            if target > matrix[TM][R]:
                T = TM + 1
            elif target < matrix[TM][L]:
                B = TM - 1
            else:
                break
            
        if not (T <= B):
            return False
        
        TM = (T+B)//2

        
        while L <= R:
            mid = (L+R)//2
            if target < matrix[TM][mid]:
                R = mid - 1
            elif target > matrix[TM][mid]:
                L = mid + 1
            else:
                return True
        return False
        