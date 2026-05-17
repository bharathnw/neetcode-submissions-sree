class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        intervals.append(newInterval)

        intervals.sort()

        stack = [intervals[0]]

        for item in intervals[1:]:
            if stack and stack[-1][1] >= item[0]:
                stack[-1] = [min(stack[-1][0], item[0]), max(stack[-1][1], item[1])]
            
            else:
                stack.append(item)
        
        return stack

        