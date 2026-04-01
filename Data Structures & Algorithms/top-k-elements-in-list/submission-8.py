class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        heap = []

        for key, cnt in counter.items():
            heapq.heappush(heap, (cnt, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for item in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
        
        