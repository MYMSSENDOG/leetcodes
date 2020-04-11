import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        s = set([x for x in range(numCourses)])
        d = collections.defaultdict(set)
        for i in prerequisites:
            s.discard(i[1])
            d[i[1]].add(i[0])
        el = len(s)
        if not el:
            return False
        while el < numCourses:
            to_del = []
            for next in d:
                if d[next].issubset(s):
                    to_del.append(next)
            if not to_del:
                return False
            el += len(to_del)
            for e in to_del:
                s.add(e)
                d.pop(e)
        return True

sol = Solution()
n = 4
prerequisites = [[1,0],[2,0],[3,0],[2,1]]
print(sol.canFinish(n,prerequisites))