class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1

        while top <= bottom:
            mid = (top + bottom)//2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                while left <= right:
                    avg = (left + right)//2
                    if matrix[mid][avg] == target:
                        return True
                    elif matrix[mid][avg] > target:
                        right = avg - 1
                    else:
                        left = avg + 1
                return False

        
        return False
                                
        