class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        if len(s) == 0:
            return False
        if s[-1] == '1':
            return False

        q = deque()

        q.append(0)

        farthest = 0
        
        while q:
            index = q.popleft()

            if index == len(s)-1:
                return True
            start = max(index+minJump, farthest+1)
            for i in range(start, min(index+maxJump, len(s)-1) + 1):
                if s[i] == '0':
                    q.append(i)
                    if i == len(s) - 1:
                        return True
            farthest = index + maxJump
        return False
                
        