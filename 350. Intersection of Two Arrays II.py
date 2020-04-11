class Solution:
    def intersect(self, nums1, nums2):
        d = {}
        for i in nums1:
            d[i] = 1 if i not in d else d[i]+1
        ret = []
        for i in nums2:
            if i in d and d[i] >0:
                ret.append(i)
                d[i] -=1
        return ret

sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersect(nums1,nums2))