class Solution:
    def wordPattern(self, pattern, str) -> bool:
        words = str.split(" ")
        if len(words) != len(pattern):
            return False
        dic_p = {}
        dic_w = {}
        for i, p in enumerate(pattern):
            word = words[i]
            if p not in dic_p and word not in dic_w:
                dic_p[p] = word
                dic_w[word] = p
            elif (p in dic_p) ^ (word in dic_w):
                return False
            else:
                if dic_p[p] == word and dic_w[word] == p:
                    continue
                else:
                    return False
        return True

sol = Solution()
pattern = "abba"
str = "dog cat cat gg"
print(sol.wordPattern(pattern, str))