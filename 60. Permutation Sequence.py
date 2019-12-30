def factorial(n):
    ret = 1
    for i in range(1,n+1):
        ret *= i
    return ret

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ret = ""
        n_str = ""
        k -=1
        for i in range(1,n+1):
            n_str += str(i)
        for i in reversed(range(1,n+1)):
            t = k//factorial(i-1)
            ret += n_str[t]
            n_str = n_str[:t] + n_str[t+1:]
            k-=t*factorial(i-1)
        return ret
sol= Solution()
n = 5
k = 5
print(sol.getPermutation(n,k))