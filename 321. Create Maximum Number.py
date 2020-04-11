class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        ret = []
        if len(nums1) < len(nums2):
            nums2, nums1 = nums1, nums2#nums1, m이 항상 길다
        m, n = len(nums1), len(nums2)
        d1 = [[0]*(m) for _ in range(m)]
        d2 = [[0] * (n) for _ in range(n)]

        for i in range(m):#dp[i][j]는 i부터 j까지 (포함) 젤 큰거
            M = -1
            M_i = -1
            for j in range(i,m):
                if M < nums1[j]:
                    M = nums1[j]
                    M_i = j
                d1[i][j] = M_i
        for i in range(n):#dp[i][j]는 i부터 j까지 (포함) 젤 큰거
            M = -1
            M_i = -1
            for j in range(i,n):
                if M <nums2[j]:
                    M = nums2[j]
                    M_i = j
                d2[i][j] = M_i
        ite = k
        print(nums1.count(9), nums2.count(9))
        nums1_start, nums2_start = 0, 0
        nums1_end, nums2_end = m - 1, n - 1
        for _ in range(ite):
            if k >= n+1:
                nums1_end =max(m-1 - (k-(n+1)), 0) + nums1_start
            if k >= m+1:
                nums2_end =max(n-1 - (k-(m+1)),0 ) + nums2_start
            n1_i = d1[nums1_start][nums1_end]
            t1 = nums1[n1_i:]
            t2 = []
            if len(nums2)> nums2_start:
                n2_i = d2[nums2_start][nums2_end]
                t2 = nums2[n2_i:]

            if t1 > t2:
                ret.append(nums1[n1_i])
                nums1_start = n1_i +1
                m = len(nums1) - n1_i - 1
                if len(nums1)- nums1_start < len(nums2) - nums2_start:
                    nums1, nums2 = nums2, nums1
                    m, n = n, m
                    d1, d2 = d2, d1
                    nums1_start, nums2_start =  nums2_start, nums1_start
                    nums1_end, nums2_end =nums2_end, nums1_end
            elif t1 == t2:
                t1 = nums1[nums1_start: n1_i]
                t2 = nums2[nums2_start: n2_i]
                if t1<t2:
                    ret.append(nums1[n1_i])
                    nums1_start = n1_i + 1
                    m = len(nums1) - n1_i - 1
                    if len(nums1) - nums1_start < len(nums2) - nums2_start:
                        nums1, nums2 = nums2, nums1
                        m, n = n, m
                        d1, d2 = d2, d1
                        nums1_start, nums2_start = nums2_start, nums1_start
                        nums1_end, nums2_end = nums2_end, nums1_end
                else:
                    ret.append(nums2[n2_i])
                    nums2_start = n2_i + 1
                    n = len(nums2) - n2_i - 1
            else:
                ret.append(nums2[n2_i])
                nums2_start = n2_i + 1
                n = len(nums2) - n2_i - 1
            k -=1
        return ret

"""
위 방법은 틀림
다른방법 연구

"""


sol = Solution()

nums1 = [1,2,9]
nums2 = [0,8,9]
k = 3

print(sol.maxNumber(nums1, nums2, k))
