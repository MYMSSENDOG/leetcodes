import collections
class Solution:
    def minMoves2(self, nums) -> int:
        s = sum(nums)
        n = len(nums)
        nums.sort()
        same = collections.defaultdict(int)
        under = [0] * n
        over = [0] * n

        for i in nums:
            same[i] +=1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                under[i] = i
            else:
                under[i] = under[i-1]
        for i in range(n):
            over[i] = n - same[nums[i]] - under[i]

        i = 0

        while under[i] < over[i]:
            i+=1
        ret = 9999999999999
        if i - 1<0:
            ret = s - nums[i-1] * n
        else:
            border = i
            S = nums[border]
            left = i * S - sum(nums[:i])
            right = sum(nums[i:n]) - (n - i) * S
            ret = min(ret, left + right)
            border = i - 1
            S = nums[border]
            left = i * S - sum(nums[:i])
            right = sum(nums[i:n]) - (n - i) * S
            ret = min(ret, left + right)
        return ret





sol = Solution()
nums = [1,2,3,4,5,6]
print(sol.minMoves2(nums))