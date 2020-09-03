class Solution:

    def titleToNumber(self, s: str) -> int:
        n = len(s)
        ret = 0
        for c in s:
            n -= 1
            ret += (ord(c) - ord("A") + 1) * 26 ** n
        return ret
sol = Solution()
s = "AAB"
print(sol.titleToNumber(s))
"""
얼핏보면 n진수 같지만 그렇지 않다.
Z 까지 26개가 있고
AA ~ ZZ까지 다시 26 * 26개가 있다.
10진수의경우 1~10까지 10개 1~100까지 100개지만 얘는 11부터100까지 세는데 100개인 느낌
그점만 유의해서 코딩하면 된다. 

"""