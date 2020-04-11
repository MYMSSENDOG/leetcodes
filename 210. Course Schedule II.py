import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites):


        s = set([x for x in range(numCourses)])
        d = collections.defaultdict(set)
        for i in prerequisites:
            s.discard(i[1])
            d[i[1]].add(i[0])
        el = len(s)
        ret = list(s)
        if not el:
            return []
        while el < numCourses:
            to_del = []
            for next in d:
                if d[next].issubset(s):
                    to_del.append(next)
            if not to_del:
                return []
            el += len(to_del)
            for e in to_del:
                ret.append(e)
                s.add(e)
                d.pop(e)
        ret.reverse()
        return ret
sol = Solution()
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
k = 4
print(sol.findOrder(k, prerequisites))