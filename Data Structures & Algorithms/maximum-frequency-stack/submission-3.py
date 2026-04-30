class FreqStack:

    def __init__(self):
        self.freq = defaultdict(list)
        self.stack = {}
        self.maxF = 0
        

    def push(self, val: int) -> None:
        self.stack[val] = self.stack.get(val, 0) + 1
        
        if self.stack[val] > self.maxF:
            self.maxF = self.stack[val]
        
        self.freq[self.stack[val]].append(val)
        

    def pop(self) -> int:

        maxList = self.freq[self.maxF]
        item = maxList.pop()
        self.stack[item] -= 1
        if self.stack[item] == 0:
            del self.stack[item]
        if len(maxList) == 0:
            self.maxF -= 1
        return item
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()