class Solution:
    def sortArrayByParity(self, A):
        l = 0
        r = len(A) - 1
        while l < r:
            while A[l] & 1 == 0 and l < r:
                l +=1
            while A[r] & 1 == 1 and l < r:
                r -=1
            A[l], A[r] = A[r], A[l]
        return A
sol = Solution()
A = [0,2,1,3]
print(sol.sortArrayByParity(A))