class Solution:
    def minWindow(self, s: str, t: str) -> str:

        key_counter = {}

        for c in t:
            key_counter[c] = key_counter.get(c, 0) + 1
        
        need = len(key_counter)
        have = 0
        curr_counter = {}
        L = 0
        res = ""
        min_len = float("inf")

        for R, c in enumerate(s):

            curr_counter[c] = curr_counter.get(c, 0) + 1

            if c in key_counter and curr_counter[c] == key_counter[c]:
                have += 1
            
            while have >= need:
                if (R - L + 1) < min_len:
                    res = s[L:R+1]
                    min_len = R - L + 1
                
                curr_counter[s[L]] -= 1
                if s[L] in key_counter and curr_counter[s[L]] < key_counter[s[L]]:
                    have -= 1
                L += 1
        return res