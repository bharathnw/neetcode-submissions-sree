class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        for word in strs:
            count = [0]* 26
            for val in word:
                count[ord(val)-ord('a')] += 1
            group_dict[tuple(count)].append(word)
        return list(group_dict.values())