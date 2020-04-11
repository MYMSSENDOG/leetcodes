import collections
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if not k or len(nums) < 2 or t < 0:
            return False

        dic = collections.defaultdict(list)

        for i in range(len(nums)):
            index = nums[i] // (t + 1)
            if index in dic:
                for j in dic[index]:
                    if i - j <= k:
                        return True
            if index + 1 in dic:
                for j in dic[index + 1]:
                    if i - j <= k and -t <= nums[i] - nums[j] <= t:
                        return True
            if index - 1 in dic:
                for j in dic[index - 1]:
                    if i - j <= k and -t <= nums[i] - nums[j] <= t:
                        return True
            dic[index].append(i)
        return False


sol = Solution()
nums = [7,1,3]
k = 2
t = 3
print(sol.containsNearbyAlmostDuplicate(nums,k,t))
