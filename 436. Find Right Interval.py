
class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        for i in range(n):
            intervals[i] += [i]
        ret = [0] * n
        intervals.sort()
        for i, interval in enumerate(intervals):
            s, e, idx = interval
            l = i+1
            r = n-1
            m = (l + r) //2
            while l<r:
                if e == intervals[m][0]:
                    break
                elif e > intervals[m][0]:
                    l = m+1
                else:
                    r = m
                m = (l + r) // 2
            if intervals[m][0]<e:
                ret[idx] = -1
            else:
                ret[idx] = intervals[m][2]
        return ret
sol = Solution()
intervals = [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]
print(sol.findRightInterval(intervals))