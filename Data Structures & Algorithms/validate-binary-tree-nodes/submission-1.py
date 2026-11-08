class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        parents = defaultdict(int)

        for child in leftChild + rightChild:
            if child == -1:
                continue

            parents[child] += 1
            if parents[child] > 1:
                return False
        
        roots = [i for i in range(n) if parents[i] == 0]

        if len(roots) != 1:
            return False
        
        visits = set()

        stack = roots
        
        while stack:
            node = stack.pop()
            if node in visits:
                return False
            
            visits.add(node)

            for child in (leftChild[node], rightChild[node]):
                if child == -1:
                    continue
                
                stack.append(child)
        
        return len(visits) == n
    
          