class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        m = max(people)

        counter = [0] * (m+1)

        for p in people:
            counter[p] += 1
        
        index, currVal = 0, 0
        

        while index < len(people):
            while counter[currVal] == 0:
                currVal += 1
            people[index] = currVal
            counter[currVal] -= 1
            index += 1

        boats = 0

        l, r = 0, (len(people)-1)

        while l <= r:
            tot = people[l] + people[r]
            if tot <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boats += 1

        return boats



            
             