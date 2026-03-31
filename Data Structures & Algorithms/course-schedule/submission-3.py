class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        

        visits = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            
            if node in visits:
                return True
            visits.add(node)
            visiting.add(node)
            for sub in adj[node]:
                if dfs(sub) == False:
                    return False
            
            visiting.remove(node)
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True

        