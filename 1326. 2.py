class Solution:
    def minTaps(self, n: int, ranges) -> int:

        dp = [0] * (n+1)
        for i,e  in enumerate(ranges):
            if e == 0:
                continue
            start = max(0,i - e)
            end = min(n, i + e)
            for j in range(start, end + 1):
                dp[j] = max(dp[j], end - j+1)
        ret = 0
        i = 0
        while i < n+1:
            if dp[i] == 0:
                return -1
            i += dp[i]
            ret +=1
        return ret
sol = Solution()
ranges = [0,0,0,0,4,0,0,0,0]
n = 8
print(sol.minTaps(n, ranges))