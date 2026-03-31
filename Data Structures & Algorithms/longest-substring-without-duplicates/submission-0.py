class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        max_len = 0
        curr_str = []
        while right < len(s):
            if s[right] in curr_str:
                index = curr_str.index(s[right])
                print(index)
                curr_str = curr_str[index+1::]
                print('curr_str in if', curr_str)
                curr_str.append(s[right])
            else:
                curr_str.append(s[right])
            print(curr_str)
            right += 1
            max_len = max(max_len,len(curr_str))
        return max_len