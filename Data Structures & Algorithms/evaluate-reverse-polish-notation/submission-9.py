class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if not token.lstrip('-').isdigit():
                a = stack.pop() if stack else 0
                b = stack.pop() if stack else 0
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(b-a)
                elif token == '*':
                    stack.append(b*a)
                elif token == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]