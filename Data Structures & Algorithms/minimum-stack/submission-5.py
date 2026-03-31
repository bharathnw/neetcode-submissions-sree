class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        minVal = val
        if self.stack and self.stack[-1][1] < minVal:
            minVal = self.stack[-1][1]
        self.stack.append((val, minVal))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
