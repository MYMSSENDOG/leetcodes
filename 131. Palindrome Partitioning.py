class Solution:
    def partition(self, s: str):#return is like [["aa","b"], ["a","a","b"]]

        def is_palindrome(s1):
            m = len(s1)
            for i in range(m//2):
                if s1[i] != s1[~i]:
                    return False
            return True

        m = len(s)
        if m == 0:
            return [[]]
        ret = []
        for i in range(0, m):
            if is_palindrome(s[:i+1]):
                ret += [[s[:i+1]] + k for k in self.partition(s[i+1:])]
        return ret

sol = Solution()
s = "abbab"
print(sol.partition(s))