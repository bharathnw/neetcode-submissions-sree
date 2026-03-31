class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        res = 0
        maxHeap = []
        tasksDic = {}

        for task in tasks:
            tasksDic[task] = tasksDic.get(task, 0) + 1
        
        for key, val in tasksDic.items():
            maxHeap.append((-1*val, key))
        
        heapq.heapify(maxHeap)
        q = deque()

        
        while maxHeap or q:
            res += 1

            if not maxHeap:
                res = q[0][2]
            else:
                poped = heapq.heappop(maxHeap)
                if poped[0] + 1 < 0:
                    q.append((poped[0]+1, poped[1], res+n))

            while q and q[0][2] == res:
                qItem = q.popleft()
                heapq.heappush(maxHeap, (qItem[0], qItem[1]))
        return res
        
        