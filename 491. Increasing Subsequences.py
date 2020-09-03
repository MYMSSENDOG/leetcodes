class Solution:
    def findSubsequences(self, nums):
        ret = []
        d = {}
        n=  len(nums)
        for i in range(n):
            q = [ [[nums[i]], i] ]
            while q:
                for _ in range(len(q)):
                    t, idx = q.pop(0)
                    for j in range(idx+1, n):
                        if nums[j] >= t[-1]:
                            if tuple(t + [nums[j]]) in d:
                                continue
                            ret.append(t + [nums[j]])
                            q.append([t + [nums[j]], j])
                            d[tuple(t + [nums[j]])] = 0
        return ret

sol = Solution()
nums = [4, 6, 7, 7]
print(sol.findSubsequences(nums))