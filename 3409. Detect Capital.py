class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        CAPITAL = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"
        first = True
        if word[0] not in CAPITAL:
            first = False
        second = False
        if len(word)>= 2:
            next = word[1]
            if next in CAPITAL:
                second = True
            if not first and second:
                return False
            for c in word[2:]:
                if first and second:
                    if c not in CAPITAL:
                        return False
                elif first and not second:
                    if c in CAPITAL:
                        return False
                elif not first and not second:
                    if c in CAPITAL:
                        return False
        return True




sol = Solution()
word = "gG"
print(sol.detectCapitalUse(word))