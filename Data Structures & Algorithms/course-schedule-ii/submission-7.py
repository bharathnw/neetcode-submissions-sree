class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preReqs = {}

        for i in range(numCourses):
            preReqs[i] = []
        
        for crs, pre in prerequisites:
            preReqs[crs].append(pre)
        
        res = set()
        visits = set()
        out = []
        
        def topSort(crs):
            if crs in visits:
                return False
            if crs in res:
                return True
            visits.add(crs)
            for pre in preReqs[crs]:
                if topSort(pre) == False:
                    return False
            visits.remove(crs)
            res.add(crs)
            out.append(crs)
        
        for i in range(numCourses):
            if topSort(i) == False:
                return []
        
        return out
            
                    

        