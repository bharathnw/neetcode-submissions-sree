class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        sumOfAll = 0
        symbols = set()
        symbols.add('+')
        symbols.add('D')
        symbols.add('C')

        stack = []
        for op in operations:
            if op in symbols and stack:
                if op == 'C':
                    val = stack.pop()
                    sumOfAll -= val
                if op == 'D':
                    val = stack[-1]
                    stack.append(val*2)
                    sumOfAll += (val*2)
                if op == '+':
                    val = stack[-1] + stack[-2]
                    stack.append(val)
                    sumOfAll += val
            else:
                stack.append(int(op))
                sumOfAll += int(op)
        
        return sumOfAll
