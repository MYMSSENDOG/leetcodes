import bisect
class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones.sort()
        while len(stones)>1:
            f = stones.pop()
            s = stones.pop()
            if f - s == 0:
                continue
            bisect.insort(stones, f-s)

        if stones:
            return stones[0]
        return 0

sol = Solution()
stones = [2,7,4,1,8,1]
print(sol.lastStoneWeight(stones))