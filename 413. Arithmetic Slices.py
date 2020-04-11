class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        n = len(A)
        ret = 0
        s = 0

        while s < n-2:
            num = 0
            d = A[s + 1] - A[s]
            s+=1
            while s < n-1 and A[s+1] - A[s] == d:
                num +=1
                s+=1
            ret += (num * (num+ 1))//2

        return ret

sol = Solution()
A = [1,2,3,4,5]
print(sol.numberOfArithmeticSlices(A))