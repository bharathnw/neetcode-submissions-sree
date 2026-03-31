# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(left, right):
            l, r = 0, 0
            res = []
            while l < len(left) and r < len(right):
                if left[l].key <= right[r].key:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
               
            res += left[l:]
            res += right[r:]
            return res
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left, right)
        return mergeSort(pairs)   
