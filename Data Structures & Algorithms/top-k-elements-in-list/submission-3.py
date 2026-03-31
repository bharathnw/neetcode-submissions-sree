class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keyMap = {}
        output = []
        for num in nums:
            if num in keyMap:
                keyMap[num] += 1
            else:
                keyMap[num] = 1
        
        sorted_keys_desc = sorted(keyMap, key=lambda k: keyMap[k], reverse=True)
        for i in range(k):
            output.append(sorted_keys_desc[i])
        return output
        