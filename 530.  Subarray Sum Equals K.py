class Solution:
    def subarraySum(self, nums, k: int) -> int:
        n = len(nums)
        S = [0] *  (n + 1)
        for i in range(1, n+1):
            S[i] = S[i-1] + nums[i-1]# S[i] - S[j] = sum(nums[j:i])
        def helper(array):
            if len(array) <= 1:
                return array, 0
            d = len(array)//2
            l,lr = helper(array[:d])
            r,rr = helper(array[d:])
            i = len(r) - 1
            j = len(l) - 1
            ret = lr + rr
            while i >= 0 and j >= 0:
                if S[r[i]] - S[l[j]] == k:
                    rc = 1
                    lc = 1
                    while i > 0 and S[r[i]] == S[r[i-1]]:
                        i-=1
                        rc +=1
                    while j > 0 and S[l[j]] == S[l[j-1]]:
                        j-=1
                        lc +=1
                    ret += rc * lc
                    i-=1
                    j-=1
                elif S[r[i]] - S[l[j]] > k:
                    i-=1
                else:
                    j-=1
            for idx in range(len(array))[::-1]:
                if l and (not r or S[l[-1]] > S[r[-1]]):
                    array[idx] = l.pop()
                else:
                    array[idx] = r.pop()
            return array, ret
        return helper([i for i in range(len(nums)+1)])[1]

sol = Solution()
nums = [-92,-63,75,-86,-58,22,31,-16,-66,-67,420]
k = 100
print(sol.subarraySum(nums,k))