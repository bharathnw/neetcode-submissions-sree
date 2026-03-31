class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strSet = set()
        L = 0
        maxLength = 0
        for R in range(len(s)):
            while s[R] in strSet:
                strSet.remove(s[L])
                L += 1
            strSet.add(s[R])
            maxLength = max(R-L+1, maxLength)
        return maxLength
        