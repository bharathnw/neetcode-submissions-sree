class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        res = ''
        maxHeap = []

        for item in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if item[0] < 0:
                heapq.heappush(maxHeap, item)

        while maxHeap:

            cnt, mostChar = heapq.heappop(maxHeap)

            if len(res) > 1 and res[-1] == res[-2] == mostChar:
                if not maxHeap:
                    break
                secCnt, secChar = heapq.heappop(maxHeap)
                res += secChar
                secCnt += 1
                if secCnt < 0:
                    heapq.heappush(maxHeap, (secCnt, secChar))
            
            res += mostChar
            cnt += 1
            if cnt < 0:
                heapq.heappush(maxHeap, (cnt, mostChar))
        
        return res


        