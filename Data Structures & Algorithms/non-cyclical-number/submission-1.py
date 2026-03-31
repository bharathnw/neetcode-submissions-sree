class Solution:
    def isHappy(self, n: int) -> bool:

        num_set = set()

        curr = n
        while curr not in num_set:
            num_set.add(curr)
            target = 0
            while curr > 0:
                target += (curr % 10)**2
                curr = curr//10
            if target == 1:
                return True
            curr = target
        
        return False

        