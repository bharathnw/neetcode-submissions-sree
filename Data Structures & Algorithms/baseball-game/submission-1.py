class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        res = 0
        for op in operations:
            if op == 'C':
                if stack:
                    res -= stack.pop()
            elif op == '+':
                resT = 0
                for num in stack[-2:]:
                    resT += num
                stack.append(resT)
                res += resT
            elif op == 'D':
                if stack:
                    r = stack[-1]*2
                    stack.append(r)
                    res += r
            else:
                stack.append(int(op))
                res += int(op)
        return res