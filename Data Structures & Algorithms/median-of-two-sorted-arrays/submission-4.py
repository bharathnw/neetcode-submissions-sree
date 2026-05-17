class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot = len(nums1)+len(nums2)
        half = (len(nums1)+len(nums2))//2

        A, B = nums1, nums2

        if len(A) > len(B):
            B, A = A, B
        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = half - i - 2
        
            al = A[i] if i >= 0 else float('-inf')
            ar = A[i+1] if (i+1) < len(A) else float('inf')
            bl = B[j] if j >= 0 else float('-inf')
            br = B[j+1] if (j + 1) < len(B) else float('inf')

            if al <= br and bl <= ar:
                if tot % 2 == 0:
                    return (max(al, bl) + min(ar, br))/2
                return min(ar, br)
            elif al > br:
                r = i - 1
            else:
                l = i + 1
            