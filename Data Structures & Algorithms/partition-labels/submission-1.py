class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        counter = {}

        for i in range(len(s)):
            counter[s[i]] = i
        
        end = 0
        size = 0
        res = []
        for i in range(len(s)):

            end = max(end, counter[s[i]])
            size += 1

            if i == end:
                res.append(size)
                size = 0


        return res