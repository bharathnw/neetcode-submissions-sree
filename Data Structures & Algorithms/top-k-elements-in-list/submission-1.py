from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        for num in nums:
            if num in freq_dict:
                freq_dict[num] +=1
            else:
                freq_dict[num] = 1

        # Order the dicitonary based on values in reverse order
        ordered_freq = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))

        #Obtain only keys from the dictionary
        list_keys = list(ordered_freq.keys())
        return list_keys[:k]
  