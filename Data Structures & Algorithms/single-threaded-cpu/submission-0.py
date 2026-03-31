class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort(key=lambda t:t[0])

        time = tasks[0][0]
        res = []
        i = 0
        minHeap = []

        while minHeap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not minHeap:
                time = tasks[i][0]
            else:
                val, index = heapq.heappop(minHeap)
                time += val
                res.append(index)

        return res
            



