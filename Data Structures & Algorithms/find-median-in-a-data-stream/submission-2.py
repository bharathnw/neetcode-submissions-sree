class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > self.maxHeap[0]:
            heapq.heappush(self.maxHeap, num)
        else:
            heapq.heappush_max(self.minHeap, num)
        
        diff = abs(len(self.minHeap) - len(self.maxHeap))
        if diff > 1:
            if len(self.minHeap) > len(self.maxHeap):
                val = heapq.heappop_max(self.minHeap)
                heapq.heappush(self.maxHeap, val)
            else:
                val = heapq.heappop(self.maxHeap)
                heapq.heappush_max(self.minHeap, val)
        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0])/2
        elif len(self.minHeap) < len(self.maxHeap):
            return self.maxHeap[0]
        else:
            return self.minHeap[0]
        
        