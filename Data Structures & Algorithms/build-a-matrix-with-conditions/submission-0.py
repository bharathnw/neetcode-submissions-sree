class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        row_sorted = []
        col_sorted = []

        row_adj = defaultdict(list)
        col_adj = defaultdict(list)

        for above, below in rowConditions:
            row_adj[above].append(below)
        
        for left, right in colConditions:
            col_adj[left].append(right)
        


        def top_sort(i, adj, sortArr):
            if i in path:
                return False
            if i in visits:
                return True
            visits.add(i)
            path.add(i)
            for nei in adj[i]:
                if not top_sort(nei, adj, sortArr):
                    return False
            sortArr.append(i)
            path.remove(i)
            return True
        
        visits = set()

        path = set()

        for i in range(1, k+1):
            if i not in visits:
                if not top_sort(i, row_adj, row_sorted):
                    return []
        row_sorted.reverse()

        visits = set()
        path = set()
        
        for i in range(1, k+1):
            if i not in visits:
                if not top_sort(i, col_adj, col_sorted):
                    return []
        col_sorted.reverse()
        
        row_map = {}
        for i, val in enumerate(row_sorted):
            row_map[val] = i
        
        col_map = {}
        for i, val in enumerate(col_sorted):
            col_map[val] = i

        res = [[0] * k for _ in range(k)]
        for i in range(1, k+1):
            row = row_map[i]
            col = col_map[i]
            res[row][col] = i
        
        return res


        
            

            


        