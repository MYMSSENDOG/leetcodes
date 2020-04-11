import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        if k > len(s):
            return 0
        alpha = [0] * 26
        border = [-1]
        for c in s:
            index = ord(c) - ord("a")
            alpha[index] += 1
        for i in range(len(s)):
            index = ord(s[i]) - ord("a")
            if alpha[index]<k:
                border.append(i)
        border.append(len(s))
        if len(border) == 2:
            return len(s)

        return max(self.longestSubstring(s[start+1:end], k)for start, end  in zip(border, border[1:]) )

# n n 26


sol = Solution()
s = "caacaabbb"
k = 3
print(sol.longestSubstring(s,k))