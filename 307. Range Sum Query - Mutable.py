class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.dp[i] = self.dp[i-1] + nums[i]

    def update(self, i: int, val: int) -> None:
        prev = self.dp[i] -self.dp[i-1]
        for k in range(i, self.n):
            self.dp[k] += val - prev
    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i-1]



"""
segment tree :
each leaf node has one element of array
each parent node has sum of all of its leaf nodes
so, update()'s time complexity is O(logn)
sumRange()'s time complexity is O(logn)
  
"""
#using trivial dp
#sum O(n) update 1  or update O(n) sum O(1)

nums = [1,3,5]
na = NumArray(nums)
na.update(1,2)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)