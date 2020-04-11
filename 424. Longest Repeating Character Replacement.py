class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s) - 1:
            return len(s)
        ret = 0
        for C in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            letter = C
            left = k
            end = 0
            front = 0
            regional_max = 0
            while front<len(s):
                while front < len(s):
                    if s[front] != letter:
                        if not left:
                            break
                        left -=1
                    front += 1
                regional_max = max(regional_max, front-end)
                next = s.find(letter, front)
                if next != -1:
                    left = next - front
                    front = next
                    while left:
                        if s[end] != letter:
                            left -= 1
                        end += 1
                else:
                    break
            ret = max(ret , regional_max)
        return ret


sol = Solution()
s = "ABBB"
k = 2
print(sol.characterReplacement(s, k))