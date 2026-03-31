class FreqStack:

    def __init__(self):
        self.heap = []
        self.counter = defaultdict(int)
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        currCnt = self.counter.get(val, 0) + 1
        self.counter[val] = currCnt
        heapq.heappush(self.heap, (-1*currCnt, -1*(len(self.stack)-1)))

    def pop(self) -> int:
        freq, index = heapq.heappop(self.heap)
        val = self.stack[-1*index]
        self.counter[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()