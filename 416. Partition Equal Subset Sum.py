import collections
class Solution:
    def canPartition(self, nums) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % 2 == 1:
            return False
        nums.sort()
        memo = collections.defaultdict(set)# memo [i] = index[i]부터의 subsum 들
        memo[n] = set([0])
        def helper(s, i):
            if s in memo[i]:
                return True
            if memo[i] and s not in memo[i]:
                return False
            if memo[i+1]:
                for m in memo[i+1]:
                    memo[i].add(nums[i] + m)
                    memo[i].add(m)
            else:
                for j in range(i+1, n):
                    if helper(s, j) or helper(s-nums[i], j):
                        return True
            return False
        return helper(s//2, 0)


nums = [1,1,3]
sol = Solution()
print(sol.canPartition(nums))
