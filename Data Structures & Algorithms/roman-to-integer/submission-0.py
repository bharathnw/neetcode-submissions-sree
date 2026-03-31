class Solution:
    def romanToInt(self, s: str) -> int:


        mappings = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        res = []
        for c in reversed(s):
            if res and res[-1] > mappings[c]:
                curr = res.pop()
                res.append(curr - mappings[c])
            else:
                res.append(mappings[c])
        return sum(res)
        