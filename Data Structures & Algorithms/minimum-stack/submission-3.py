class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        _, minVal = self.stack[-1]
        self.stack.append((val, val if minVal > val else minVal))
        

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
