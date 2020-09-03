class Solution:
    def stringMatching(self, words):
        ret = []
        words.sort(key = lambda x : len(x))
        for i in range(len(words)):
            s1 = words[i]
            for j in range(i+1, len(words)):
                s2 = words[j]
                if s1 in s2:
                    ret.append(s1)
                    break
        return ret

sol = Solution()
words = ["mass","as","hero","superhero"]
print(sol.stringMatching(words))