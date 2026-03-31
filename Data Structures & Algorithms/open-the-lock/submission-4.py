class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadend = set(deadends)

        if target in deadend or '0000' in deadend:
            return -1
        
        if target == '0000':
            return 0
        
        visits = set()

        q = deque(['0000'])

        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                item = q.popleft()
                for i in range(4):
                    currPos = str((int(item[i]) + 1 + 10)%10)
                    nextLockPos = item[:i] + currPos + item[i+1:]
                    if nextLockPos not in deadend and nextLockPos not in visits:
                        q.append(nextLockPos)
                        visits.add(nextLockPos)
                    if nextLockPos == target:
                        return res
                        
                    currNeg = str((int(item[i]) - 1 + 10)%10)
                    nextLockNeg = item[:i] + currNeg + item[i+1:]
                    if nextLockNeg not in deadend and nextLockNeg not in visits:
                        q.append(nextLockNeg)
                        visits.add(nextLockNeg)
                    if nextLockNeg == target:
                        return res
        
        return -1
                    



                

        


                
        