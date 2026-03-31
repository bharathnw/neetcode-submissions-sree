class MinStack:

    def __init__(self):
        self.stack = []
        self.minValuesStack = []
    

    def push(self, val: int) -> None:
        if len(self.minValuesStack) == 0:
            self.minValuesStack.append(val)
        elif self.minValuesStack[-1] >= val:
            self.minValuesStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minValuesStack[-1]:
            self.minValuesStack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValuesStack[-1]

        
        
