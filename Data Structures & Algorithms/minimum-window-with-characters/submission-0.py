class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window, search = {}, {}

        for c in t:
            search[c] = search.get(c, 0) + 1

        l, r = 0, 0

        need = len(search)
        have = 0

        minLength = float('inf')
        left = 0

        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in search and search[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < minLength:
                    minLength = r-l+1
                    left = l
                window[s[l]] -= 1
                if s[l] in search and search[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
            r += 1
        
        return "" if minLength == float('inf') else s[left: left+minLength]

        