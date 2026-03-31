class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = {}

        for task in tasks:
            counter[task] = counter.get(task, 0) + 1
        
        heap = []
        for key, count in counter.items():
            heap.append((-1 * count, key))

        heapq.heapify(heap)

        q = deque([])
        res = 0
        while heap or q:
            res += 1
            if heap:
                cnt, item = heapq.heappop(heap)
                currCnt = (cnt * -1) - 1
                if currCnt > 0:
                    q.append((-1*currCnt, item, res + n))
            
            if q and q[0][2] == res:
                qCnt, qItem, qCyc = q.popleft()
                heapq.heappush(heap, (qCnt, qItem))
        return res
