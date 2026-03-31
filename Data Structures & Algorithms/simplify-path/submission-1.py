class Solution:
    def simplifyPath(self, path: str) -> str:


        pathArr = path.split('/')
        stack = []
        for s in pathArr:
            if s == '' or s == '.':
                continue
            if s == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return '/'+'/'.join(stack)