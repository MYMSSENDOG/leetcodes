import collections
class Solution:
    def frogPosition(self, n: int, edges, t: int, target: int) -> float:
        d1= collections.defaultdict(list)
        d2 = collections.defaultdict(list)
        dp = [0] * n
        dp[0] = 1
        s = set([1])
        q = [1]
        for fr, to in edges:
            d1[fr] += [to]
            d1[to] += [fr]
        while q:
            for i in range(len(q)):
                temp = q.pop(0)
                for child in d1[temp]:
                    if child not in s:
                        s.add(child)
                        d2[temp] +=[child]
                        q.append(child)
        q = [1]
        time = 0
        while q:
            for i in range(len(q)):
                temp = q.pop(0)
                if temp == target:
                    if time == t or (time < t and not len(d2[temp])):
                        return dp[temp-1]
                    else:
                        return 0
                for child in d2[temp]:
                    dp[child-1] = dp[temp-1] / len(d2[temp])
                    q.append(child)
            time+=1


n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4
sol = Solution()
print(sol.frogPosition(n,edges,t,target))