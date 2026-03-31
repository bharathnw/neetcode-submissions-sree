class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = set(['*', '-', '+', '/'])

        stack = []

        for num in tokens:
            if num not in ops:
                stack.append(int(num))
            else:
                a = stack.pop()
                b = stack.pop()
                if num == '*':
                    stack.append(b * a)
                if num == '+':
                    stack.append(a+b)
                if num == '-':
                    stack.append(b - a)
                if num == '/':
                    stack.append(int(b/a))
        return stack[-1]
        