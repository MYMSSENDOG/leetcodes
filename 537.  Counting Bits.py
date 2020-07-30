class Solution:
    def countBits(self, num: int):
        dp = [0]
        if num < 1:
            return dp[:num + 1]
        iter = 1
        cur = 1
        while cur <= num:
            for i in range(iter):
                dp.append(dp[cur - iter] + 1)

                cur+=1
            iter *=2
        return dp[:num + 1]



sol = Solution()
n = 8
print(sol.countBits(n))