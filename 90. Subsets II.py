class Solution:
    def subsetsWithDup(self, nums):
        ret =[[]]
        a = set()
        def comb(nums, k):
            if k == 0:
                return [[]]
            else:
                return [pre + [e] for i,e in enumerate(nums[k-1:],k-1) for pre in comb(nums[:i], k - 1)]
        for i in range(1,len(nums) + 1):
            ret+= (comb(nums,i))
        for i in ret:
            i.sort()
            a.add(tuple(i))
        return a




sol = Solution()
Input= [1,2,2]
print(sol.subsetsWithDup(Input))