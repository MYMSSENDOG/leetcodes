class Solution:
    def subsetsWithDup(self, nums):
        a = dict()
        for i in nums:
            a[i]  = a[i] + 1 if i in a else  1

        single = []
        multi = []
        single_ret = [[]]
        for i in a:
            if a[i] == 1:
                single.append(i)
            else:
                multi.append([i,a[i]])

        def comb(nums, k):
            if k == 0:
                return [[]]
            else :
                return [pre + [e] for i, e in enumerate(nums[k-1:],k-1) for pre in comb(nums[:i],k-1)]


        def add(multi):
            if not multi:
                return [[]]
            else:
                return [ [multi[0][0]] *i +  pre for i in range(multi[0][1] + 1) for pre in add(multi[1:])]


        for i in range(1,len(single) + 1):
            single_ret+= (comb(single,i))

        return [i + m for i in single_ret for m in add(multi)]

sol = Solution()
Input = [1,2,2,3,3]
print(sol.subsetsWithDup(Input))