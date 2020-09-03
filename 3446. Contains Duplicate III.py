class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) < 2 or k == 0:
            return False

        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        nums.sort()

        r = 1
        l = 0
        r_val, r_idx = nums[r]
        l_val, l_idx = nums[l]

        while r < len(nums):
            if l == r:
                r += 1
                if r < len(nums):
                    r_val, r_idx = nums[r]
                else:
                    return False
            if r_val - l_val <= t:
                if abs(r_idx - l_idx) <= k:
                    return True
                r += 1
                if r < len(nums):
                    r_val, r_idx = nums[r]
            else:
                l += 1
                l_val, l_idx = nums[l]
        return False


sol = Solution()
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(sol.containsNearbyAlmostDuplicate(nums,k,t))
