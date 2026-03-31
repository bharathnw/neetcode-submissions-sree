class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        courses = {}
        pre = defaultdict(set)
        visits = set()

        for preR, crs in prerequisites:
            pre[crs].add(preR)

        def dfs(i):
            if i in visits:
                return pre[i]

            dep = pre[i]
            if not dep:
                return set()
            
            res = set()
            for item in dep:
                res = res | dfs(item)
            pre[i] |= res
            visits.add(i)
            return pre[i]
            
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for uj, vj in queries:
            if uj in pre[vj]:
                res.append(True)
            else:
                res.append(False)
        
        return res
            
        
        





        