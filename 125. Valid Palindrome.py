class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            while not (s[l].isalpha() or s[l].isalnum()):
                l +=1
            while not s[r].isalpha() or s[r].isalnum():
                r -= 1
            if s[l].capitalize() != s[r].capitalize():
                return False
            else:
                l +=1
                r -= 1
        return True


sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))