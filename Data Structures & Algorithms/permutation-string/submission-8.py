class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Map = {}

        if len(s2) < len(s1):
            return False

        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1
        
        L = 0
        window_map = {}

        for R in range(len(s2)):
            if s2[R] not in s1Map:
                L = R + 1
                window_map = {}
                continue
    
            window_map[s2[R]] = window_map.get(s2[R], 0) + 1
            
            while window_map[s2[R]] > s1Map[s2[R]]:
                window_map[s2[L]] -= 1
                L += 1

            if window_map == s1Map:
                return True

        return False