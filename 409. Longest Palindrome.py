import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.defaultdict(int)
        for c in s:
            d[c] +=1
        ret = 0
        odd = False
        for i, e in d.items():
            if e >=2:
                ret += e//2 * 2
            if e % 2 == 1:
                odd = True
        if odd:
            ret +=1
        return ret



sol = Solution()
s = "abcccddc"
print(sol.longestPalindrome(s))