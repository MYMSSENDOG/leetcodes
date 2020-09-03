import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.defaultdict(int)
        is_odd = False
        ret = 0
        for c in s:
            d[c] += 1
        for c in d:
            if d[c]%2 == 1:
                is_odd = True
            ret += d[c] // 2
        ret *= 2
        if is_odd:
            ret += 1
        return ret
sol = Solution()
s = "abccccdd"
print(sol.longestPalindrome(s))
