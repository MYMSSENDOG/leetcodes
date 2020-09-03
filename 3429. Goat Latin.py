class Solution:
    def toGoatLatin(self, S: str) -> str:
        ret = ""
        words = S.split()
        for i,word in enumerate(words,1):
            if word[0] in "aeiouAIOEU":
                ret += word + "ma" + "a" * i
            else:
                ret += word[1:] + word[0] +  "ma" + "a" * i
            if i < len(words):
                ret += " "
        return ret


S =  "I speak Goat Latin"
sol = Solution()
print(sol.toGoatLatin(S))