class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-1*stone for stone in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            st1 = -1 * heapq.heappop(heap)
            st2 = -1 * heapq.heappop(heap)

            diff = abs(st1-st2)
            if diff > 0:
                heapq.heappush(heap, -1 * diff)
        
        return 0 if len(heap) == 0 else -1 * heap[0]
        