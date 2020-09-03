class Solution:
    def isPalindrome(self, s: str) -> bool:
        ret = ""
        for c in s:
            if c.isalpha():
                ret+=c.capitalize()
            elif c.isnumeric():
                ret+=c
        if ret == ret[::-1]:
            return True
        return False

sol = Solution()
s = "P"
print(sol.isPalindrome(s))