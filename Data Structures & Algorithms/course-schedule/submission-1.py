class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visits = set()

        preCourse = {}

        for crs, pre in prerequisites:
            if crs not in preCourse:
                preCourse[crs] =  [pre]
            else:
                preCourse[crs].append(pre)

        def dfs(crs):
            if crs in visits:
                return False
            if crs in preCourse and preCourse[crs] == []:
                return True
            
            visits.add(crs)
            if crs in preCourse:
                for pre in preCourse[crs]:
                    if not dfs(pre):
                        return False
            visits.remove(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        