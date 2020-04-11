class Solution:
    def intersection(self, nums1, nums2):
        d = {}
        for i in nums1:
            if i not in d:
                d[i] = 1
        ret = []
        for i in nums2:
            if i in d and d[i] == 1:
                ret.append(i)
                d[i] = 0
        return ret
sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersection(nums1,nums2))