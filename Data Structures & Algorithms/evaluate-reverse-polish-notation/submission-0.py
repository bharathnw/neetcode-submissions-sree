class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():  # Check if token is a number (positive or negative)
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "*":
                    stack.append(b * a)
                elif token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "/":
                    # Perform integer division
                    stack.append(int(b / a))
        return stack.pop()
