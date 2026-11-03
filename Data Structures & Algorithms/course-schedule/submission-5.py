class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)

        for crs, pr in prerequisites:

            adj[crs].append(pr)

        visited = set()
        safe = set()

        def dfs(i):
            if i in visited:
                return False
            if i in safe:
                return True
            
            visited.add(i)

            for crs in adj[i]:
                if dfs(crs) == False:
                    return False
                
            visited.remove(i)
            safe.add(i)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True
        