class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for i in range(len(s)):

            if s[i] == ']':
                chars = ''
                num = ''
                while stack and stack[-1] != '[':
                    chars = stack.pop() + chars
                stack.pop()

                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * chars)

            else:
                stack.append(s[i])
        
        return ''.join(stack)
            
