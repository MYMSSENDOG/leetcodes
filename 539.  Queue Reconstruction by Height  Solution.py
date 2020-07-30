class Solution:
    def reconstructQueue(self, people):
        ret = [[] for _ in range(len(people))]
        idx = [x for x in range(len(people))]
        people.sort(key = lambda x: [x[0],-x[1]])
        while people:
            cur = people.pop(0)
            h, k = cur

            id = idx.pop(k)
            ret[id] = cur
        return ret

sol = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(sol.reconstructQueue(people))
