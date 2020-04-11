class Solution:
    def rotate(self, nums, k: int) -> None:
        def gcd(n1, n2):
            M = max(n1,n2)
            m = min(n1,n2)
            d = M%m
            while d != 0:
                M = m
                m = d
                d = M%m
            return m
        n = len(nums)
        k = k%n
        if not k:
            return 
        #1
        i = 0
        j = 0
        outer = gcd(n, k)
        inner = n //outer


        for i in range(outer):
            start = i
            t = nums[start]
            next = start + k
            for j in range(inner):
                nv = nums[next]
                nums[next] = t
                t = nv
                next = (next + k)%n
        print(nums)



sol = Solution()
nums = [1,2,3,4,5,6,7,8]
k = 4
sol.rotate(nums,k)