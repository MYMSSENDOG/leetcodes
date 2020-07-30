class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        d = 10 ** 9 + 7
        if k >m:
            return 0
        #m C k
        def helper(start, end, minimum, maximum, k):
            if k == 0:
                return min(maximum, minimum) ** (end - start + 1)
            if start == end:
                if minimum < maximum:
                    return maximum - minimum
                else:
                    return 0
            if end - start + 1 > maximum - minimum:
                return 0
            elif end - start + 1 == maximum - minimum:
                return 1


            d = (end - start) // 2
            ret = 0
            for m in range(minimum, maximum+1):# min  보다 1이상 크고 맥스보다 작거나 같고
                for j in range(k):
                    l = helper(start, start+d, minimum, m, j)
                    r = helper(start+d+1, end, m, maximum, k-j)
                    ret += l * r
                    ret %=  ((10 ** 9) + 7)
            return ret
        return helper(0,n-1, 0, m, k)

sol = Solution()
n = 2
m = 3
k = 1
print (sol.numOfArrays(n,m,k))