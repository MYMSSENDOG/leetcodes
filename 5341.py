class Solution:
    def maxEvents(self, events) -> int:
        for i in range(len(events)):
            events[i][0],events[i][1] =events[i][1],events[i][0]
        events.sort()
        for i in range(len(events)):
            events[i][0], events[i][1] = events[i][1], events[i][0]
        d = {}
        ret = 0
        for s, e in events:
            for i in range(s, e+1):
                if i not in d:
                    d[i] = 1
                    ret +=1
                    break
        return ret




sol = Solution()
events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
print(sol.maxEvents(events))
