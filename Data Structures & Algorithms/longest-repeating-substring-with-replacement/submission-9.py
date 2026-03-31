class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        preMap = {}
        maxLn = 0
        L = 0
        res = 0
        for R in range(len(s)):

            preMap[s[R]] = 1 + preMap.get(s[R], 0)
            maxLn = max(maxLn, preMap[s[R]])

            while (R-L+1) - maxLn > k:
                preMap[s[L]] -= 1
                L += 1
            res = max(res, R-L+1)

        return res
            
        