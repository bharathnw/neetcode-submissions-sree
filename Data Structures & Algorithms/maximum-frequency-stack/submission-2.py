class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.maxCnt = 0
        self.counter = {}
        

    def push(self, val: int) -> None:
        currCnt = self.counter.get(val, 0) + 1
        self.counter[val] = currCnt
        if currCnt > self.maxCnt:
            self.maxCnt = currCnt
            self.stacks[currCnt] = []
        self.stacks[currCnt].append(val)
        

    def pop(self) -> int:
        lastItem = self.stacks[self.maxCnt].pop()
        self.counter[lastItem] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return lastItem

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()