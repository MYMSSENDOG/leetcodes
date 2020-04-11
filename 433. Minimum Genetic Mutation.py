class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:
        if end not in bank:
            return False

        s = set(bank)
        if start in s:
            s.remove(start)
        q = [start]
        ret = 0
        while q:
            for _ in range(len(q)):
                t = q.pop(0)
                if t == end:
                    return ret
                for i in range(len(t)):
                    for new_c in "ACGT":
                        new_combi = t[:i] + new_c + t[i+1:]
                        if new_combi in s:
                            s.remove(new_combi)
                            q.append(new_combi)
                        else:
                            continue
            ret +=1
        return -1

sol = Solution()
start ="AAAAAAAA"
end=  "CCCCCCCC"
bank=["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA","CCCCCCCC"]



print(sol.minMutation(start, end, bank))