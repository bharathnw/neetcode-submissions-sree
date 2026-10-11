class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                if token == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a)+int(b))
                
                if token == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b)-int(a))
                
                if token == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a)*int(b))
                
                if token == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b)/int(a))
            else:
                stack.append(token)
        
        return int(stack[0])
            


        