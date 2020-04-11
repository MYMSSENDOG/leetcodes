class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        ret = 0
        cur_team = [set([i])for i in range(n)]
        dp = [[speed[i],efficiency[i]] for i in range(n)]

        ret = max(dp[i][0] * dp[i][1] for i in range(n))
        for _ in range(k-1):
            for i in range(n):
                next_per = 0
                next_mate = -1
                for j in range(n):
                    if j in cur_team[i]:
                        continue
                    this_per = (speed[j] + dp[i][0]) * min(efficiency[j], dp[i][1])
                    if this_per> next_per:
                        next_mate = j
                        next_per = this_per

                cur_team[i].add(next_mate)
                dp[i][0] += speed[next_mate]
                dp[i][1] = min(dp[i][1], efficiency[next_mate])

            ret = max(ret, max(dp[i][0] * dp[i][1] for i in range(n)))
        return ret%(10**9+7)
    # O(n^2 * k)
sol = Solution()
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
print(sol.maxPerformance(n,speed,efficiency,k))