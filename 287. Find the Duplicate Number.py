class Solution:
    def findDuplicate(self, nums):
        def helper(m,M):
            while 1:
                mid = (M + m) / 2
                cnt_l, cnt_r, cnt_m = 0, 0, 0
                for i in nums:
                    if i == mid:
                        cnt_m += 1
                    elif M >= i > mid:
                        cnt_r += 1
                    elif m <= i < mid:
                        cnt_l += 1

                if cnt_m > 1:
                    return mid
                if cnt_r == cnt_l:
                    a = helper(m,int(mid-0.5))
                    b = helper(int(mid+0.5), M)
                    if a:
                        return a
                    if b:
                        return b
                elif cnt_r > cnt_l:
                    m = int(mid + 0.5)
                elif cnt_r < cnt_l:
                    M = int(mid-0.5)
                a = helper(m,M)
                if a:
                    return a
                return None


        n = len(nums)
        M = n - 1
        m = 1
        return int(helper(m,M))


sol = Solution()
nums = [3,3,1,4,3,3]
print(sol.findDuplicate(nums))