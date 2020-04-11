class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** (1 / 2))


sol = Solution()
n = 3
print(sol.bulbSwitch(n))