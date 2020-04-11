import collections
class Solution:
    def frogPosition(self, n: int, edges, t: int, target: int) -> float:
        d = collections.defaultdict(list)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for fr, to in edges:
            d[fr] += [to]
            d[to] += [fr]
        q = [1]
        time = 0
        while q:

            for i in range(len(q)):
                temp = q.pop(0)
                for c in d[temp]:
                    if temp != 1:
                        if len(d[temp]) == 1:
                            dp[c] = dp[temp]
                        else:
                            dp[c] = dp[temp]/(len(d[temp]) - 1)
                    else:
                        dp[c] = dp[temp] / (len(d[temp]))
                    q.append(c)
                    if c == target:
                        if t == time+1:
                            return dp[c]
                        elif len(d[c])==1 and t>time:
                            return dp[c]
                        else:
                            return 0
            time +=1
        return 0



sol = Solution()
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 20
target =6
print(sol.frogPosition(n,edges,t,target))
