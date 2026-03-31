class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if self.minHeap and num > (-1 * self.minHeap[0]):
            heapq.heappush(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, -1 * num)
            
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))
            else:
                heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
        

    def findMedian(self) -> float:
        if not self.minHeap and not self.maxHeap:
            return 0
        if len(self.minHeap) == len(self.maxHeap):
            return ((-1 * self.minHeap[0]) + self.maxHeap[0])/2.0
        if len(self.minHeap) > len(self.maxHeap):
            return -1 * self.minHeap[0]
        else:
            return self.maxHeap[0]
        