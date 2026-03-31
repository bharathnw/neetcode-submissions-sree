class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        L = 0 
        out = 0
        maxCount = 0
        for R in range(len(s)):
            char_map[s[R]] = char_map.get(s[R], 0) + 1
            maxCount = max(maxCount, char_map[s[R]])
            while R - L + 1 - maxCount  > k:
                char_map[s[L]] -= 1
                L += 1
            out = max(out, R-L+1)
        return out
                

        