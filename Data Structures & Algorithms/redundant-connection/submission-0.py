class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = {}
        rank = {}

        for node, edge in edges:
            if node not in parent:
                parent[node] = node
                rank[node] = 0
            if edge not in parent:
                parent[edge] = edge
                rank[edge] = 0

        def find(node):
            if parent[node] == node:
                return node
            else:
                found = find(parent[node])
                parent[node] = found
                return found

        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                parent[p1] = p2
            elif rank[p2] < rank[p1]:
                parent[p2] = p1
            else:
                parent[p1] = p2
                rank[p2] += 1
            return True
        for num, edge in edges:
            if not union(num, edge):
                return [num, edge]



            

