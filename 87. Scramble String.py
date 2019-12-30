class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if s1 == s2:
            return True
        if ''.join(sorted(s1)) != ''.join(sorted(s2)):
            return False
        for i in range(1,n):
            if self.isScramble(s1[:i ], s2[:i]) and self.isScramble(s1[i :], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False
sol = Solution()
s1 = "great"
s2 = "rgtae"
print(sol.isScramble(s1,s2))