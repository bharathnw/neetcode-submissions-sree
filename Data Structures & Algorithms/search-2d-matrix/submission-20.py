class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for item in matrix:
            L = 0
            R = len(item) - 1
            if target >= item[L] and target <= item[R]:
                while L <= R:
                    mid = (L + R) // 2
                    print(target, item[mid])
                    if target < item[mid]:
                        R = mid - 1
                    elif target > item[mid]:
                        L = mid + 1
                    else:
                        return True
                return False
            else:
                continue
        return False

                
        