class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        res = 0
        hashmap = {}
        maxF = 0
        for R in range(len(s)):
            hashmap[s[R]] = hashmap.get(s[R], 0) + 1
            maxF = max(maxF, hashmap[s[R]])

            while R-l+1 - maxF > k:
                hashmap[s[l]] -= 1
                l += 1
            res = max(R-l+1, res)
        
        return res

