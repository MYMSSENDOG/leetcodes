class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.dp = [0] * (len(self.nums)+1)
        for i ,e in enumerate(self.nums):
            self.dp[i] = self.dp[i - 1] + e
    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i-1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)