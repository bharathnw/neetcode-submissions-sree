class Solution:
    def isValid(self, s: str) -> bool:

        mapper = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        stack = []

        for c in s:
            if c == '{' or c == '(' or c == '[':
                stack.append(c)
            elif stack and stack[-1] == mapper[c]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
        