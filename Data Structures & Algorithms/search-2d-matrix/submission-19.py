class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for item in matrix:
            print(item)
            output = False
            L = 0
            R = len(item) - 1
            print(target, item[L], item[R])
            if target >= item[L] and target <= item[R]:
                print('success')
                while L <= R:
                    mid = (L + R) // 2
                    print(target, item[mid])
                    if target < item[mid]:
                        print(R,'before')
                        R = mid - 1
                        print(R, 'after')
                    elif target > item[mid]:
                        L = mid + 1
                    else:
                        return True
                return False
            else:
                continue
        return False

                
        