class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        d = {}
        def helper(s1, s2):
            if not s1 or not s2:
                return 0
            s1, s2 = max(s1,s2), min(s1,s2)
            if (s1,s2) in d :
                return d[(s1,s2)]

            if s1[0] == s2[0]:
                return 2 + helper(s1[1:], s2[1:])
            n = len(s1)
            M = 0
            for i in range(n):
                idx = s2.find(s1[i])
                if idx >=0:
                    M = max(M, 2 + helper(s2[idx+1:], s1[i+1:]))
            d[(s1,s2)] = M
            return M

        M = 0
        for i in range(n):
            s1 = s[:i][::-1]
            s2 = s[i + 1:]
            M =  max(1 +helper(s1,s2), M)
        for i in range(n):
            s1 = s[:i][::-1]
            s2 = s[i:]
            M =  max(helper(s1,s2), M)
        return M





sol = Solution()
s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
print(sol.longestPalindromeSubseq(s))