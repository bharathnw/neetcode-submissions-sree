class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []

        for x, y in points:
            dis = ((x**2) + (y**2))**(0.5)
            heapq.heappush(maxHeap, (-1*dis, (x,y)))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []

        for _, (x, y) in maxHeap:
            res.append([x,y])
        
        return res
        