class Solution:
    def numTimesAllBlue(self, light) -> int:
        n = len(light)
        b = [0] * n
        dp = [0] * (n +1)
        dp[-1] = 1
        start = 0
        ret = 0
        for i,e in enumerate(light):
            b[e-1] = 1

            while start < n and b[start] != 0 and dp[start-1] == 1:
                if b[start] and dp[start-1] == 1:
                    dp[start] = 1
                    start +=1
                else:
                    break
            if dp[i] == 1:
                ret +=1

        return ret

sol = Solution()
light = [2,1,4,3,6,5]
print(sol.numTimesAllBlue(light))