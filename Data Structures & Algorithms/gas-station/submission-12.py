class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        profits = [gas[i] - cost[i] for i in range(len(gas))]

        print(profits)

        tank = 0
        total = 0
        start = 0
        for i in range(len(gas)):
            tank += profits[i]
            total += profits[i]
            if tank < 0:
                tank = 0
                start = i+1
        
        return start if total >= 0 else -1


