class Solution:
    def minimumPushes(self, word: str) -> int:
        
        mapper = {}

        for c in word:
            # cnt = (len(mapper) // 8) + 1
            mapper[c] = mapper.get(c, 0) + 1

        if len(mapper) <= 8:
            return len(word)
        
        heap = []
        for k, v in mapper.items():
            heapq.heappush(heap, (-1 * v, k))
        res = 0
        cnt = 0
        while heap:
            v, k = heapq.heappop(heap)
            res += (-1 * v) * ((cnt // 8) + 1)
            cnt += 1
        
        return res






