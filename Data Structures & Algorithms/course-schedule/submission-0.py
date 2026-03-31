
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visits = set()

        def dfs(course):
            if course in visits:
                return False
            if preMap[course] == []:
                return True
            visits.add(course)
            for cr in preMap[course]:
                if not dfs(cr):
                    return False 
            visits.remove(course)
            preMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        