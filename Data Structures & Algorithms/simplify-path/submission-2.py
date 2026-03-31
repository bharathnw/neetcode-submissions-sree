class Solution:
    def simplifyPath(self, path: str) -> str:

        pathArr = path.split('/')

        stack = []

        for index, item in enumerate(pathArr):
            if item == '..':
                if stack:
                    stack.pop()
                continue
            
            if item == '.' or item == '':
                continue
            stack.append(item)

        
        return  '/'+'/'.join(stack)
            
        