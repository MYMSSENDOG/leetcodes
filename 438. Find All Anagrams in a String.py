import collections
class Solution:
    def findAnagrams(self, s: str, p: str):
        n = len(s)
        m = len(p)
        ret = []


        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        for c in p:
            d1[c] += 1
        i = 0
        j = 0

        while j < n or i < n-m+1:
            if j-i<m:
                cur = s[j]
                if cur in d1:
                    d2[cur] +=1
                    j+=1
                else:
                    d2 = collections.defaultdict(int)
                    i = j+1
                    j = i
            else:
                for ch, count in d2.items():
                    if d1[ch] != count:
                        break
                else:
                    ret+=[i]
                prev = s[i]
                d2[prev] -=1
                i +=1

        return ret


s = "cbaebabacd"
p = "abc"
sol = Solution()
print(sol.findAnagrams(s,p))