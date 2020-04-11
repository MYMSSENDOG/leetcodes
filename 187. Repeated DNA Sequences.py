from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s)<=10:
            return []
        dict = defaultdict(int)
        for i in range(10, len(s)+1):
            t = s[i-10:i]
            dict[t] +=1
        ret = []
        for i in dict:
            if dict[i]>1:
                ret.append(i)
        return ret
sol = Solution()
s = "AAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))