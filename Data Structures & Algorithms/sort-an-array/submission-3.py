class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr)//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            i, j = 0, 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            if i < len(left):
                res = res + left[i:]
            if j < len(right):
                res = res + right[j:]
            return res
        
        return mergeSort(nums)
