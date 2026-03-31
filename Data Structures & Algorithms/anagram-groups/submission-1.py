class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyMap = {}
        output = []
        for strval in strs:
            sortedVal = ''.join(sorted(strval))
            if sortedVal in keyMap:
                keyMap[sortedVal].append(strval)
            else:
                keyMap[sortedVal] = [strval]
        return list(keyMap.values())