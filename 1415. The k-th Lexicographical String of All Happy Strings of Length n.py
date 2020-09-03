class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 길이 l 이라 하면 3 * 2 ** (l-1)
        if k > 3 * (2 **(n-1)):
            return ""
        ret = ""
        alpha = "abc"
        k-=1
        d = 2 **(n-1)
        r = k // d
        ret += alpha[r]
        for i in range(1, n):
            k %= d
            d//=2
            r = k // d# 0 or 1
            p = ret[-1]
            if r == 0:
                if p == "a":
                    ret+= "b"
                else:
                    ret += "a"
            elif r == 1:
                if p == "c":
                    ret +="b"
                else:
                    ret +="c"
        return ret


sol = Solution()
n = 10
k = 100
print(sol.getHappyString(n,k))