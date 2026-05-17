class Solution:
    def romanToInt(self, s: str) -> int:

        mapper = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        stack = []

        for c in s:
            if not stack:
                stack.append(mapper[c])
                continue
            if stack[-1] < mapper[c]:
                stack[-1] = (mapper[c] - stack[-1])
            else:
                stack.append(mapper[c])
        
        return sum(stack)