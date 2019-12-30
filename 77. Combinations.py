class Solution:
    def combine(self, n: int, k: int):
        if k == 0:
            return [[]]

        return [pre + [i] for i in range(k,n+1) for pre in self.combine(i-1,k-1)]

sol = Solution()
print(sol.combine(4,2))