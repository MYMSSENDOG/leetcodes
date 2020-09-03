import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        for c in ransomNote:
            d1[c] +=1
        for c in magazine:
            d2[c] +=1

        for i, e in d1.items():
            if d2[i] < e:
                return False

        return True


sol = Solution()
ransomNote = "aa"
magazine = "aab"
print(sol.canConstruct(ransomNote, magazine))