class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r_grp = deque([])
        d_grp = deque([])

        for i, c in enumerate(senate):
            if c == 'R':
                r_grp.append(i)
            else:
                d_grp.append(i)
        
        while len(r_grp) > 0 and len(d_grp) > 0:
            r, d = r_grp.popleft(), d_grp.popleft()

            if r < d:
                r_grp.append(len(senate) + r)
            else:
                d_grp.append(len(senate) + d)
        
        return 'Dire' if len(d_grp) > 0 else 'Radiant'

