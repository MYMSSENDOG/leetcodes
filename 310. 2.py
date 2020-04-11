import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges):
        d = collections.defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        s = set(range(n))
        while len(s)>2:
            s2 = set()
            for i in s:
                if len(d[i]) == 1:
                    s2.add(i)
            if s2:
                for j in s2:
                    t = d[j][0]
                    d[j].remove(t)
                    d[t].remove(j)
            s = s- s2
        return list(s)



sol = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(sol.findMinHeightTrees(n, edges))