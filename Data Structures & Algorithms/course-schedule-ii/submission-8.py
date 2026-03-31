class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []

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
            for crs in adj[node]:
                if dfs(crs) == False:
                    return False
            visiting.remove(node)
            res.append(node)

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return res
            
        