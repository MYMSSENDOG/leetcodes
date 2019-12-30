class Solution:
    def merge(self, nums1 , m: int, nums2, n: int) -> None:
        if not n:
            return

        m -=1
        n -=1
        k = m + n + 1
        while m > -1 and n > -1:
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m -=1
            else:
                nums1[k] = nums2[n]
                n -=1
            k-=1
        nums1[:n+1] = nums2[:n+1]
        print(nums1)
sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(sol.merge(nums1,m,nums2,n))