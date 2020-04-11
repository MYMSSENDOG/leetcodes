class Solution:
    def minMoves2(self, nums) -> int:
        s = sum(nums)
        n = len(nums)
        nums.sort()
        s_m_s = [0] * n
        s_m_s[0] = 2 * nums[0] - s
        for i in range(1,n):
            s_m_s[i] = s_m_s[i-1] + nums[i] * 2
        i = n-2
        while i >= 0:
            if nums[i] == nums[i+1]:
                s_m_s[i] = s_m_s[i+1]
            i-=1
        s_m_s+=[-s]
        ret = 99999999
        under_border = nums[0]
        prev = nums[0]
        for i in range(0,n):
            if nums[i] != prev:
                under_border = prev
            S = nums[i]
            ret = min(ret, abs(2 * i * S - n * S - s_m_s[i - 1]))
            S -= 1
            while S > under_border:
                ret = min(ret, abs(2 * i * S - n * S- s_m_s[i-1]))
                S-=1
            prev = nums[i]
        return ret
        #return min(2 * a * S - sum(nums[0:a]) + sum(nums[a:n]))



sol = Solution()
nums = [1,1,1]
print(sol.minMoves2(nums))