class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        L = 0
        currSum = 0
        output = 0
        for R in range(len(arr)):
            currSum += arr[R]
            if R - L >= k:
                currSum -= arr[L]
                L += 1
            if R >= k-1 and currSum/k >= threshold:
                output += 1
            
        return output
