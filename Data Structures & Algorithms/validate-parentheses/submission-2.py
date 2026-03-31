class Solution:
    def isValid(self, s: str) -> bool:

        paren_dict = {')': '(',  '}':'{', ']':'[' }
        stack = []
        for char in s:
            if char in paren_dict and len(stack) > 0:
                if stack[-1] != paren_dict[char]:
                    return False
                else:
                    out = stack.pop()
                    
            else:
                stack.append(char)
        print(stack)
        if len(stack) > 0:
            return False
        return True