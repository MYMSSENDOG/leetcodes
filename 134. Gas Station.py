class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        m = len(gas)

        t = 0
        start = 0

        for i in range(m):
            t += gas[i] - cost[i]
            if t<0:
                start = i+1
                continue
        return start






sol = Solution()
gas = [2,0,3]
cost = [1,2,2]
print(sol.canCompleteCircuit(gas,cost))