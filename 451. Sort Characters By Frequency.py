import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        """
        d = collections.defaultdict(int)
        d2 = collections.defaultdict(list)

        n = len(s)
        ret = ""
        for c in s:
            d[c] +=1
        for i, e in d.items():
            d2[e] += [i]

        for i in  range(n,0,-1):
            for c in d2[i]:
                ret += c * i
        return ret
        """
        A = [[i, 0] for i in range(26)]
        for c in s:
            idx = ord(c) - ord("a")
            A[idx][1] +=1
        A.sort(key = lambda c: c[1], reverse=True)
        ret = ""
        for c, i in A:
            ret+= chr(c + ord("a")) * i
        return ret
sol = Solution()
s = "tree"
print(sol.frequencySort(s))