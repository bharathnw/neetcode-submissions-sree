class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        output = []

        l1 = 0
        l2 = 0

        while len(output) <= (len(nums1) + len(nums2)):
            if l1 >= len(nums1) or l2 >= len(nums2):
                break
            if nums1[l1] < nums2[l2]:
                output.append(nums1[l1])
                l1 += 1
            else:
                output.append(nums2[l2])
                l2 += 1

        if l1 <= len(nums1):
            for i in range(l1, len(nums1)):
                output.append(nums1[i])
        if l2 <= len(nums2):
            for i in range(l2, len(nums2)):
                output.append(nums2[i])
        
        n = len(output)
        mid = n // 2

        if n % 2 == 1:
            return output[mid]
        else:
            return (output[mid - 1] + output[mid]) / 2