class Solution:
    def pancakeSort(self, A):
        n = len(A)
        ret = []
        for i in range(n)[::-1]:
            idx = A.index(n) + 1
            if idx == n:
                n -= 1
                continue
            else:
                if idx != 1:
                    ret.append(idx)
                    A[:idx] = A[:idx][::-1]
                ret.append(i + 1)
                A[:n] = A[:n][::-1]
            n-=1
        return ret

A = [2,1,3]
sol = Solution()
print(sol.pancakeSort(A))