class Solution:
    def combinationSum3(self, k: int, n: int):
        def helper(array, k, n):
            if k == 1:
                t = n - sum(array)

                s = 0
                if len(array) == 0:
                    s = 0
                else:
                    s = array[-1]

                if t>s and t not in array and t < 10:
                    return [array + [t]]
            if sum(array) > n:
                return []
            start = 1
            if array:
                start = array[-1]
            return [x for i in range(start, 10) for x in helper(array + [i], k-1, n) if i not in array]
        if sum(range(9,9-k,-1)) < n:
            return []
        if sum(range(1,1+k))>n:
            return []
        return helper([], k, n)


sol = Solution()
k = 3
n = 7
print(sol.combinationSum3(k,n))