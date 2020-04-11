import collections
import bisect
class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        es_array = sorted([[efficiency[i], speed[i]] for i in range(n)])
        #se_array = sorted([[speed[i], efficiency[i]] for i in range(n)])
        #d = collections.defaultdict(list)# n log n
        #for e,s in es_array:
         #   d[e] +=[s]# n memory n
        cur_speeds = []
        ret = 0
        cur_sum = 0
        prev = es_array[n-k][0]
        for i in range(n-1, -1,-1):
            min_eff = es_array[i][0]
            if i >= n-k:
                cur_speeds.append(es_array[i][1])
                cur_sum += es_array[i][1]
                ret = max(ret, min_eff * cur_sum)#k
                continue
            if i == n-k-1:
                cur_speeds.sort()#k log k
            #if min_eff == prev:
                #continue
           # for s in d[min_eff]:
            s = es_array[i][1]
            if s > cur_speeds[0]:
                bisect.insort(cur_speeds, s) #len(s) * logk
                cur_sum += s
            while len(cur_speeds)>k:
                min_speed = cur_speeds.pop(0)# 1
                cur_sum -= min_speed
            prev = min_eff
            ret = max(ret, cur_sum * min_eff)
        return ret%(10**9+7)
#o nlog n but don't cought in TLE
sol = Solution()
n = 3
speed = [2,8,2]
efficiency = [2,7,6]
k = 2
print(sol.maxPerformance(n,speed,efficiency,k))