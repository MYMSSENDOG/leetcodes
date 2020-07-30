import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        d = collections.defaultdict(list)
        s = set()
        for a, b in prerequisites:
            d[a].append(b)
            s.add(a)

        while s:
            cur = s.pop()
            q = [[cur]]
            for _ in range(len(q)):
                to_del = set()
                t = q.pop()
                last = t[-1]
                for next in d[last]:
                    if next in t:
                        return False
                    if next in to_del or next not in s:
                        continue
                    t.append(next)
                    to_del.add(next)
                    q.append(t)
                s -= to_del
        return True

sol = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.canFinish(numCourses, prerequisites))