class Solution:
    def merge(self, intervals):
        ret = []
        if len(intervals)<=1:
            return intervals
        intervals.sort()
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if cur_end< intervals[i][0]: # 만약 끊어진다면
                ret.append([cur_start,cur_end])
                cur_start = intervals[i][0]
                cur_end = intervals[i][1]
            else:
                cur_end = max(cur_end,intervals[i][1])
            if i == len(intervals) - 1:
                ret.append([cur_start, cur_end])
        return ret        

nums = [[1,4],[4,5]]
sol = Solution()
print(sol.merge(nums))