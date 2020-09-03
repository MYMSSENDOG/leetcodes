import collections
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = collections.defaultdict(int)
        for c in J:
            d[c] = 1
        return sum(d[s] for s in S)

J = "aA"
S = "aAAbbbb"
sol = Solution()
print(sol.numJewelsInStones(J, S))
