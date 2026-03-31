class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        minHeap = []

        for i, num in enumerate(arr):
            heapq.heappush(minHeap, (abs(num-x), i))
        
        newRes = []
        for _ in range(k):
            heapq.heappush(newRes, arr[heapq.heappop(minHeap)[1]])
        res = []
        for _ in range(k):
            res.append(heapq.heappop(newRes))
        
        return res


        