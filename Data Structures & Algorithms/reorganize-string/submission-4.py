class Solution:
    def reorganizeString(self, s: str) -> str:
        
        res = ''

        counter = {}

        maxHeap = []

        for c in s:
            counter[c] = counter.get(c, 0) + 1
        
        for key, val in counter.items():
            heapq.heappush(maxHeap, (-1 *val, key))
        prev = None
        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            if res and res[-1] == char:
                return ""
            res += char
            currCnt = (-1 * cnt) - 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if currCnt == 0:
                continue
            prev = (-1 * currCnt, char)
        
        return res if prev is None else ""

        
