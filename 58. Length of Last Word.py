class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ret = 0
        s = s.rstrip()
        for i in reversed(range(len(s))):
            if s[i] != " ":
                ret +=1
            else:
                break
        return ret


nums = "sd asdasd    "
sol = Solution()
print(sol.lengthOfLastWord(nums))