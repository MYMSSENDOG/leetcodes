class Solution:
    def totalHammingDistance(self, nums ) -> int:
        n = len(nums)
        bit = [2 ** j for j in range(32)]
        q = [n] * 32
        for i in range(n):
            for j in range(32):
                if bit[j] & nums[i]:#1이면 하나 줄인다
                   q[j] -=1

        return sum(q[k] * (n - q[k]) for k in range(32))
sol = Solution()
nums = [4,14,2]
print(sol.totalHammingDistance(nums))