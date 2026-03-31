class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {']':'[', '}':'{', ')':'('}
        
        for i in range(len(s)):
            if s[i] in pairs:
                if len(stack) > 0 and stack[-1] == pairs[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return True if not stack else False
                

