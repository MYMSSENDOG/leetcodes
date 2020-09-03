import collections
class Solution:
    def findMaxLength(self, nums) -> int:
        d = collections.defaultdict(list)
        o, z = 0,0
        d[0] = [-1]
        ret=  0
        for i in range(len(nums)):
            if nums[i] == 1:
                o +=1
            else:
                z+=1
            d[o-z].append(i)
        for i in range(len(nums)//2):
            if i in d:
                ret = max(ret, d[i][-1] - d[i][0])
            if -i in d:
                ret = max(ret, d[-i][-1] - d[-i][0])
        return ret



sol = Solution()
nums = [0,0,0,0,1]
print(sol.findMaxLength(nums))