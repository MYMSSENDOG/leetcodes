import collections
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        d = collections.defaultdict(list)
        for i in range(len(manager)):
            d[manager[i]] += [i]
        q= [[-1,0]]
        ret = 0
        while q:
            for _ in range(len(q)):
                t = q.pop(0)
                m_ids, time = d[t[0]], t[1]
                for m_id in m_ids:
                    if d[m_id]:
                        q.append([m_id, time+informTime[m_id]])
                    else:
                        ret = max(ret, time)

        return ret



n = 4
headID = 2
manager = [3,3,-1,2]
informTime = [0,0,162,914]
sol = Solution()
print(sol.numOfMinutes(n,headID,manager,informTime))
