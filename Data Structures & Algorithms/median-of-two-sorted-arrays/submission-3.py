class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        output = []

        l1 = 0
        l2 = 0
        index = 0
        n = len(nums1) + len(nums2)
        while (l1+l2) <= n / 2:
            if l1 > len(nums1) or l2 > len(nums2):
                break
            if l1 >= len(nums1):
                output.append(nums2[l2])
                l2 += 1
                continue
            elif l2 >= len(nums2):
                output.append(nums1[l1])
                l1 += 1
                continue

            if nums1[l1] < nums2[l2]:
                output.append(nums1[l1])
                l1 += 1
            else:
                output.append(nums2[l2])
                l2 += 1

        print(output)
        
        if n % 2 == 1:
            return output[-1]
        else:
            return (output[-1]  + output[-2]) / 2