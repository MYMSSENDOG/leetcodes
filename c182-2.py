class Solution:
    def numTeams(self, rating) -> int:
        n = len(rating)
        dp = [0] * n
        if n < 3:
            return 0
        ret = 0
        dp2 = [0] * n
        for i in range(1,n):
            count = 0
            for j in range(i):
                if rating[i] > rating[j]:
                    count +=1
            dp[i] = count
        for i in range(2,n):
            cur = rating[i]
            for j in range(i):
                prev = rating[j]
                if cur > prev:
                    ret += dp[j]

        for i in range(n-2,-1,-1):
            count = 0
            for j in range(n-1,i,-1):
                if rating[i] > rating[j]:
                    count+=1
            dp2[i] = count

        for i in range(n-3,-1,-1):
            cur = rating[i]
            for j in range(n-1,i,-1):
                prev = rating[j]
                if cur>prev:
                    ret += dp2[j]
        return ret


sol = Solution()
rating = [1,2,3,4]
print(sol.numTeams(rating))