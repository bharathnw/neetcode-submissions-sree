class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        l = 0
        satisfied = 0
        window = 0
        max_window = 0
        for r in range(len(customers)):

            if grumpy[r] == 0:
                satisfied += customers[r]
            else:
                window += customers[r]
            
            if r - l + 1 > minutes:
                if grumpy[l] == 1:
                    window -= customers[l]
                l += 1
            
            max_window = max(max_window, window)
        
        return satisfied + max_window

            


        