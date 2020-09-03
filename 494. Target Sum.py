import collections
class Solution:
    def findTargetSumWays(self, nums, S):
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        n = len(nums)

        d1[0] = 0
        def dfs1(cur, idx):
            if idx == n//2:
                d1[cur] +=1
                return
            dfs1(cur + nums[idx], idx+1)
            dfs1(cur - nums[idx], idx+1)

        def dfs2(cur, idx):
            if idx == n:
                d2[cur] += 1
                return
            dfs2(cur + nums[idx], idx+1)
            dfs2(cur - nums[idx], idx+1)
        dfs1(0, 0)
        dfs2(0,n//2 )
        return sum(e * d2[S-i]for i, e in d1.items())


sol = Solution()
nums = [1,1,1,1,1]
S = 3
print(sol.findTargetSumWays(nums, S))
