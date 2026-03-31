class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        L = 0
        R = len(matrix)-1

        while L <= R:
            M = (L+R)//2
            if target < matrix[M][0]:
                R = M-1
            elif target > matrix[M][len(matrix[M])-1]:
                L = M+1
            else:
                so = matrix[M]
                sl = 0
                sr = len(so) -1
                while sl <= sr:
                    sm = (sl+sr)//2
                    if target < so[sm]:
                        sr = sm-1
                    elif target > so[sm]:
                        sl = sm+1
                    else:
                        return True
                return False
        return False






        