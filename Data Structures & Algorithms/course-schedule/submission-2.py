class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_map = {}

        for i in range(numCourses):
            course_map[i] = []

        for crs, pre in prerequisites:
            course_map[crs].append(pre)

        visits = set()

        def dfs(crs):
            if crs in visits:
                return False
            visits.add(crs)
            for preReq in course_map[crs]:
                if dfs(preReq) == False:
                    return False
            visits.remove(crs)
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True
        

            

               