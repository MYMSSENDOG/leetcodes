class Solution:
    def makesquare(self, nums) -> bool:
        if not nums:
            return False
        s = sum(nums)
        if s % 4 != 0 :
            return False
        n = s // 4
        nums.sort()

        def helper(cur_sum, left_line, arr, idx):
            if left_line == 1:
                return True
            for i in range(idx, len(arr)):
                if cur_sum +  arr[i] < n:
                    if i > 0 and arr[i-1] == arr[i]:
                        continue
                    if helper(cur_sum +  arr[i], left_line, arr[:i] + arr[i+1:],i):
                        return True
                elif cur_sum +  arr[i] == n:
                    if helper(0, left_line-1, arr[:i] + arr[i + 1:],0):
                        return True
                else:
                    break
            return False
        if nums[0] == n:
            return helper(0,3,nums[1:],0)
        return helper(nums[0],4,nums[1:],0)



sol = Solution()
nums = [1,1,2,2,2]
print(sol.makesquare(nums))