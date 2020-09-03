class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        ret = duration if timeSeries else 0
        for i in range(1,len(timeSeries)):
            ret += duration
            if timeSeries[i] - timeSeries[i - 1]< duration:
                ret -= duration - (timeSeries[i] - timeSeries[i - 1])
        return ret


sol = Solution()
nums = [1,2]
d = 2
print(sol.findPoisonedDuration(nums,d))