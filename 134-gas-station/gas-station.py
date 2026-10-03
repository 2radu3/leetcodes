class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        if sum(gas) < sum(cost): return -1

        gas_curr = 0
        idx = 0
        for i in range(len(gas)):
            gas_curr += gas[i] - cost[i]
            if gas_curr < 0:
                gas_curr = 0
                idx = i + 1
        return idx
