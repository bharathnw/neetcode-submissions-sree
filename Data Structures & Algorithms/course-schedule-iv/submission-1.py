class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        mapper = {}

        def dfs(crs):
            if crs in mapper:
                return mapper[crs]
            mapper[crs] = set()
            for pre in adj[crs]:
                mapper[crs].add(pre)
                mapper[crs].update(dfs(pre))   
            return mapper[crs]
        
        for i in range(numCourses):
            dfs(i)
        res = []
        for pre, crs in queries:
            res.append(True if pre in mapper[crs] else False)

        return res
        