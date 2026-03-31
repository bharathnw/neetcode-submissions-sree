class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visits = set()
        output = 0
        L = 0
        for R in range(len(s)):
            while s[R] in visits:
                visits.remove(s[L])
                L += 1 
            visits.add(s[R])
            output = max(output, R-L+1)
        return output

