import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        d = collections.defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        route = []
        min_level = 9999
        ret = []
        if len(edges) == 1:
            return edges[0]
        for i in range(n):
            if len(d[i]) == 1:
                continue
            route.append([i])
            level = 1
            while route and level<=min_level:
                for j in range(len(route)):
                    t = route.pop(0)
                    cur = t[-1]
                    prev = t[-1]
                    if len(t)>1:
                        prev = t[-2]
                    for k in d[cur]:
                        if  k != prev:
                            route.append(t + [k])
                if route:
                    level +=1
                else:
                    if level < min_level:
                        min_level = level
                        ret = [i]
                    elif level == min_level:
                        ret.append(i)
                    else:
                        continue
        return ret
    

sol = Solution()
n = 4
edges =[[1,0],[1,2],[1,3]]

print(sol.findMinHeightTrees(n,edges))