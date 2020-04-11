class Solution:
    def isPossible(self, target) -> bool:
        target.sort()
        c = len(target)
        one = [1] * len(target)

        def helper(start, c):
            visited = []


            for i in one[start:]:
                if i in visited:
                    continue
                visited.append(i)
                if c > target[start]:
                    break
                if target[start] == 2*c - i:
                    return helper(start+1, 2*c - i)
                else:
                    tf = helper(start+1, 2*c - i)
                    if tf:
                        return tf

            return False

        for i ,e in enumerate(one):
            if target[i] == 1:
                continue
            if c>target[i]:
                return False
            elif c == target[i]:
                one[i] = c
                c = c*2 - e
            else:
                return helper(i, c)
        return True


sol = Solution()

target = [8,5]
print(sol.isPossible(target))
"""


a b c d e ...
2*sum - i

"""