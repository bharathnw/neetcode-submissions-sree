from collections import deque
class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        
        self.graph[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph:
            vals = self.graph[src]
            for val in vals:
                if val == dst:
                    self.graph[src].remove(val)
                    return True
            
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        def dfs(src, dst, adjList, visits):
            if src in visits:
                return False
            if src == dst:
                return True
            
            visits.add(src)
            for neighbor in adjList.get(src, []):
                if dfs(neighbor, dst, adjList, visits):
                    return True  
            return False

        return dfs(src, dst, self.graph, set())


    

