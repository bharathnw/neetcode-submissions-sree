class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        q = deque(['0000'])
        steps = 0

        if target in deadends or '0000' in deadends:
            return -1
        visits = set(['0000'])

        while q:
            steps += 1 
            for _ in range(len(q)):
                item = q.popleft()
                for i in range(4):
                    for j in [1,-1]:
                        num = int(item[i])
                        num += j
                        if num > 9:
                            num = 0
                        if num < 0:
                            num = 9
                        lock = item[:i] + str(num) + item[i+1:]
                        if lock in deadends or lock in visits:
                            continue
                        if lock == target:
                            return steps
                        visits.add(lock)
                        q.append(lock)
        
        return -1
        