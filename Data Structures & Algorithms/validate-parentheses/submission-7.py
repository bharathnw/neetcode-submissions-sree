class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'}':'{', ')':'(', ']':'['}
        stack = []
        

        for c in s:
            if c in dic:
                if len(stack) > 0 and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0



        