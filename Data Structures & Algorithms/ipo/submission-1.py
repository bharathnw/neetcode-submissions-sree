class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        minHeap = [(capital[i], i) for i in range(len(capital))]
        maxHeap = []

        heapq.heapify(minHeap)
        
        for _ in range(k):
            while minHeap and w >= minHeap[0][0]:
                heapq.heappush(maxHeap, -1*profits[heapq.heappop(minHeap)[1]])
            
            if not maxHeap:
                break
            
            w += (-1*heapq.heappop(maxHeap))
        
        return w

            


        