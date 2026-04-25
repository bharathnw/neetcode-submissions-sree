class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        heap = []

        for i in range(len(profits)):
            heapq.heappush(heap,(capital[i], profits[i]))
        
        capacity_heap = []        
        for _ in range(k):
            while heap and heap[0][0] <= w:
                heapq.heappush(capacity_heap, -1 * heapq.heappop(heap)[1])
            
            if not capacity_heap:
                return w
            
            w += (-1 * heapq.heappop(capacity_heap))
        
        return w

        