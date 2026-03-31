class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        result = set()
        visits = set()
        out = []
        def dfs(crs):
            if crs in visits:
                return False
            if crs in result:
                return True
            visits.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visits.remove(crs)
            result.add(crs)
            out.append(crs)
            return True

        for num in range(numCourses):
            if not dfs(num):
                return []
            
        return out
            

            
        