class Solution:
    def subsets(self, nums):
        ret = [[]]

        def comb(array, k):
            if k == 0:
                return [[]]
            return [pre + [e] for i,e in enumerate(array[k-1:],k-1) for pre in comb(array[:i], k - 1)]

        for i in range(1,len(nums)+1):
            ret += comb(nums,i)
        return ret

nums = [1,2,3]
sol = Solution()
print(sol.subsets(nums))