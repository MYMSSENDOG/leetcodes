class Solution:
    def findNthDigit(self, n: int) -> int:
        dp = [0] * 11
        ten = 1

        for i in range(1, len(dp)):
            dp[i] = i * 9 * ten
            ten *= 10
        s = 0
        for i in range(len(dp)):
            s += dp[i]
            if s >= n: # i자리수
                s -= dp[i]
                ret = (n - s - 1) // i + 10 ** (i - 1) #i자리의  번째 숫자의
                 # 번째 수
                for k in range(i - 1 - (n - s - 1) % i):
                    ret //=10
                return ret % 10

        """"
        ~9
        
        한개씩
        10~   10개는 1 +  0~9
            다음 10개는 2 + 0~9
        1 9개
        10 90개 * 2
        100 900개  * 3 
        1000 9000개.... * 4
        .. .90000 * 5
        """

sol = Solution()
n = 35
print(sol.findNthDigit(n))