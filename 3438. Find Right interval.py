class Solution:
    def findRightInterval(self, intervals):
        for i, interval in enumerate(intervals):
            interval.append(i)
        s_intervals = sorted(intervals)
        intervals.sort(key = lambda x : x[1])
        e_intervals = intervals
        s_idx = 0
        ret = [-1] * len(intervals)
        for s, e, idx in e_intervals:
            while s_idx < len(s_intervals) and s_intervals[s_idx][0] < e:
                s_idx += 1
            if s_idx < len(s_intervals):
                ret[idx] = s_intervals[s_idx][2]
        return ret



intervals = [[1,4],[2,3],[3,4]]
sol = Solution()
print(sol.findRightInterval(intervals))