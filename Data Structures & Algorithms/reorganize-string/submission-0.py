class Solution:
    def reorganizeString(self, s: str) -> str:
        
        prev = None

        maxHeap = []

        cnt = {}

        res = ""

        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        
        maxHeap = [(-count, c) for c, count in cnt.items()]

        heapq.heapify(maxHeap)

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = (cnt, char)
            
        return res


            



