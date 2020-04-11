class Solution:
    def getSkyline(self, buildings):
        if not buildings or not buildings[0]:
            return []
        ret = [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0], [9999999999999, 0]]
        for i, coord in enumerate(buildings[1:], 1):
            l, r, h = coord
            j = 0
            to_fix = []

            #초입
            while ret[j][0] <= l:
                j += 1
            if ret[j-1][0] == l:
                if ret[j-1][1]<h:
                    if j-2>=0 and ret[j-2][1] == h:
                        to_fix.append([j-1,"p"])
                    else:
                        to_fix.append([j-1,"f"])
                l_index = -1
            else:
                if ret[j - 1][1] >= h:
                    l_index = -1
                    pass
                else:
                    l_index = j  # 나중에 j 위치에 l h 삽입
            #중간
            while ret[j][0] < r:
                if ret[j][1] <= h:
                    if ret[j - 1][1] <= h:
                        to_fix.append([j, "p"])
                    else:
                        if r != ret[j][0] :
                            to_fix.append([j, "f"])
                j += 1

            # r 삽입할 위치  = to pop 이고 현재 to pop 은 r보다 오른쪽이다
            #막타
            if ret[j-1][1] >= h:
                pass
            elif ret[j][0] == r:
                pass

            else:
                ret.insert(j, [r, ret[j - 1][1]])

            if l_index != -1:
                ret.insert(l_index, [l, h])

            while to_fix:
                t, f = to_fix.pop(-1)
                if l_index != -1:
                    t += 1
                if f == "f":
                    ret[t][1] = h
                else:
                    ret.pop(t)
        return ret[:-1]




sol = Solution()
buildings =[[3,10,20],[3,9,19],[3,8,18],[3,7,17],[3,6,16],[3,5,15],[3,4,14]]
print(sol.getSkyline(buildings))