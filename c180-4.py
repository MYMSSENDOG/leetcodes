class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        cur_team = set()
        cur_performance = 0
        cur_speed = 0
        cur_eff = 0
        next_speed = 0
        next_eff = 0
        next_i = 0
        ret = 0
        for _ in range(k):
            if _ == 0:
                for i in range(n):
                    if speed[i] * efficiency[i] > cur_performance:
                        cur_performance = speed[i] * efficiency[i]
                        cur_speed = speed[i]
                        cur_eff = efficiency[i]
                        next_i = i
                cur_team.add(next_i)
                ret = max(ret, cur_performance)
            else:
                next_perform = 0
                for i in range(n):
                    if i in cur_team:
                        continue
                    if (cur_speed + speed[i]) * min(cur_eff, efficiency[i])> next_perform:
                        next_i = i
                        next_perform = (cur_speed + speed[i]) * min(cur_eff, efficiency[i])
                        next_speed = speed[i]
                        next_eff = efficiency[i]
                cur_performance = next_perform
                cur_speed += next_speed
                cur_eff = min(cur_eff, next_eff)
                cur_team.add(next_i)
                ret = max(ret, cur_performance)

        return ret%(10**9+7)
sol = Solution()
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k= 2
print(sol.maxPerformance(n,speed,efficiency,k))
# speed 의 총합 * 그들의 효율 중 최하