class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key = lambda intervals: [intervals[1],intervals[0]])
        n = len(intervals)
        if not intervals or not intervals[0]:
            return 0
        end = intervals[0][1]
        count = 1
        for s, e in intervals[1:]:
            if s >= end:
                count +=1
                end = e
        return n -count

sol = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(sol.eraseOverlapIntervals(intervals))
