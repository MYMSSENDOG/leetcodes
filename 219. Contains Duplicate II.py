class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        if not k or len(nums) < 2:
            return False
        dic = {}

        for i,e  in enumerate(nums):
            if e in dic:
                if i - dic[e] <=k:
                    return True
            dic[e] = i
        return False

sol = Solution()
nums = [1,2,3,1,2,3]
k = 2
print(sol.containsNearbyDuplicate(nums,k))