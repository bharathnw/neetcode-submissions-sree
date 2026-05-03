class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i, task in enumerate(tasks):
            task.append(i)

        heap = []

        i = 0

        tasks.sort(key=lambda t : t[0])

        time = tasks[0][0]

        res = []

        while i < len(tasks) or heap:
            
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not heap:
                time =  tasks[i][0]
                continue
            
            dur, index = heapq.heappop(heap)
            time += dur
            res.append(index)
        
        return res





        