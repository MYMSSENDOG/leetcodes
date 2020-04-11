class Solution:
    def maxProduct(self, words) -> int:
        ret = 0
        d = {}
        for w in words:
            hex = 0
            for c in [ord(c) - 97 for c in w]:
                hex |= 1 << c
            d[w] = hex
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                w1, w2 = words[i], words[j]
                if (d[w1] & d[w2]) == 0:
                    ret = max(ret, len(w1) * len(w2))
        return ret

sol = Solution()
words = ["a","ab","abc","d","cd","bcd","abcd"]
print(sol.maxProduct(words))