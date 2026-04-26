class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        res = ''
        temp = None
        while heap:

            if len(res) > 1 and heap[0][1] == res[-1] == res[-2]:
                temp = heapq.heappop(heap)
            if not heap:
                break
            cnt, c = heapq.heappop(heap)
            res += c
            newCnt = (-1*cnt) - 1
            if newCnt > 0:
                heapq.heappush(heap, (-newCnt, c))
            if temp:
                heapq.heappush(heap, temp)
                temp = None
        
        return res


