class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        heap = []

        for x, y in points:
            dis = (x**2 + y**2)
            heap.append((dis, [x,y]))
        
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        