class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        RSenate = deque()
        DSenate = deque()

        for i, party in enumerate(senate):
            if party == 'D':
                DSenate.append(i)
            else:
                RSenate.append(i)
        
        while RSenate and DSenate:
            if RSenate[0] < DSenate[0]:
                RSenate.append(len(senate) + RSenate.popleft())
                DSenate.popleft()
            else:
                DSenate.append(len(senate)+ DSenate.popleft())
                RSenate.popleft()

        return 'Dire' if DSenate else 'Radiant'




        