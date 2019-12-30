class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        def insert_merage(array, a):
            left = 0
            right = len(array) - 1
            while left + 1 <right:
                mid = (left + right) // 2
                if array[mid]<=a:
                    left = mid
                else:
                    right = mid
            if array[left] > a:
                array.insert(left,a)
                return left
            elif array[right]<a:
                array.insert(right+1,a)
                return right+1
            else:
                array.insert(right ,a)
                return right

        """
        m,n  = len(nums1), len(nums2)
        if n>m:
            nums1, nums2 = nums2, nums1
            m,n  = n,m
        #range =
        if n == 0:
            if m % 2 == 1:
                return nums1[m//2]
            else:
                return (nums1[m//2 - 1] + nums1[m//2])/2
        ml, mr = 0, m
        nl, nr = 0, n-1
        mm = 0
        nm = 0
        while nl +1 <nr:
            mm = (ml + mr) // 2
            nm = (nl + nr) // 2
            if nums1[mm] == nums2[nm]:
                return nums1[mm]
            if nums1[mm] > nums2[nm]:
                mr -= nm - nl
                nl = nm
            else:
                ml += nr-nm
                nr = nm
       # if nums1[mm] == nums2[nm]:
        #    return nums1[mm]
        print("nums1 = " , nums1[mm],nums1[mm-1])
        print("nums1 = " , nums2[nm], nums2[nm+1])
        """
        m,n  = len(nums1), len(nums2)
        if n>m:
            nums1, nums2 = nums2, nums1
            m,n  = n,m
        for i in nums2:
            t = insert_merage(nums1,i)
            if t >= (m + n) //2:
                break
        if (m + n) % 2 == 0:
            return (nums1[(m + n)//2] + nums1[(m + n)//2-1])/2
        else:
            return nums1[(m + n)//2]
sol = Solution()
n1 = [1,2,3,5,6,7]
n2 = [4,8,9,10]
print(sol.findMedianSortedArrays(n1,n2))