class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        i = 0
        res = ''
        while i < len(s):
            chars = ''
            num = ''
            while s[i].isdigit():
                num = num + s[i]
                i += 1
            stack.append(num)
            num = 0
            if s[i] == ']':
                while stack and stack[-1] != '[':
                    chars = stack.pop() + chars
                stack.pop()
                num_di = stack.pop()
                chars = int(num_di) * chars
                stack.append(chars)
            else:
                stack.append(s[i])
            i += 1
        
        return ''.join(stack)

