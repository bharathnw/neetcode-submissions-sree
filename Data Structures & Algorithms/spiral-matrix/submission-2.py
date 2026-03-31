class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #Limits
        L = 0
        R = len(matrix[0]) - 1
        T = 0
        B = len(matrix) - 1
        res = []
        while L <= R and T <= B:
           
            for c in range(L, R+1):
                res.append(matrix[T][c])
            T += 1

            for c in range(T, B+1):
                res.append(matrix[c][R])
            R -= 1

            if not (L <= R and T <= B):
                break

            for c in range(R, L-1, -1):
                res.append(matrix[B][c])
            B -= 1

            for c in range(B, T-1, -1):
                res.append(matrix[c][L])
            L += 1

        return res


        