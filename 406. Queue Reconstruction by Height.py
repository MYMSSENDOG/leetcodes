import collections
class Solution:
    def reconstructQueue(self, people):
        d = collections.defaultdict(list)
        #people.sort(key = lambda p : [p[1],p[0]])
        heights = []
        for h, k in people:
            if h not in d:
                heights.append(h)
            d[h].append(k)
        heights.sort(reverse= True)
        ret = []
        for h in heights:
            d[h].sort()
            for order in d[h]:
                ret.insert(order, [h,order])

        return ret
sol = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(sol.reconstructQueue(people))