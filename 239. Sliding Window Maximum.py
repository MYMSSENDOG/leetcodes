import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        q = []
        ret = []
        # deque 에 적절한 후보를 유지시킨다. 
        for i,n in enumerate(nums):
            if q and nums[q[-1]] < n:
                while q and nums[q[-1]] <n:
                    q.pop()
            q += [i]
            if q[0] <= i-k:
                q.pop(0)
            if i >= k-1:
                ret += [nums[q[0]]]
        return ret
sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k= 2
print(sol.maxSlidingWindow(nums,k))
