class Solution:
    def reformat(self, s: str) -> str:
        num = ""
        char = ""
        ret = ""
        for c in s:
            if c.isnumeric():
                num+=c
            if c.isalpha():
                char+=c
        if max(len(num),len(char)) - min(len(num),len(char)) >1:
            return ""
        if len(num) > len(char):
            for i in range(len(char)):
                ret += num[i]
                ret+=char[i]
            ret+=num[-1]
        elif len(num) < len(char):
            for i in range(len(num)):
                ret += char[i]
                ret += num[i]
            ret+=char[-1]
        else:
            for i in range(len(num)):
                ret += char[i]
                ret += num[i]
        return ret
s = "a0b1c2"
sol = Solution()
print(sol.reformat(s))