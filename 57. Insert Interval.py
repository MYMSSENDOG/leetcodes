class Solution:
    def insert(self, intervals, newInterval):
        left = [i for i in intervals if i[1]<newInterval[0]]
        right = [i for i in intervals if i[0]>newInterval[1]]
        s = newInterval[0]
        e = newInterval[1]
        if left + right != intervals: #한쪽끝이아니면
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[-1 - len(right)][1])
        return left + [[s,e]] + right



nums = [[1,3],[6,9]]
newInterval = [2,5]
sol = Solution()
print(sol.insert(nums,newInterval))
