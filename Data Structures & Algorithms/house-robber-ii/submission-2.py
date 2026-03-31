class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        phase1 = nums[:len(nums)-1]
        phase2 = nums[1:]

        def tryRob(phase):
            if not phase:
                return 0
            if len(phase) == 1:
                return phase[0]
            one = phase[0]
            sec = max(one, phase[1])

            for num in phase[2:]:
                temp = sec
                sec = max(one+num, sec)
                one = temp
            return sec
            
        return max(tryRob(phase1), tryRob(phase2))
