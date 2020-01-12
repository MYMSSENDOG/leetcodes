class Solution:
    def getSkyline(self, buildings):
        ret = [ [buildings[0][0], buildings[0][2]], [buildings[0][1], 0], [9999999999999, 0]]
        for i, coord in enumerate(buildings[1:], 1):
            l_valid = False
            r_valid = False
            to_fix = []
            l_pos = 0
            r_pos = 0
            r_h = 0
            l, r, h = coord
            j = 0
            while ret[j][0] <= l:
                j += 1
                pass
            if ret[j - 1][1] >= h:
                pass
            else:
                l_valid = True
                l_pos = j
                #ret.insert(j, [l,h])

            to_pop = j  # r 은 여기부터 검사

            while ret[to_pop][0] <= r:
                if ret[to_pop][1] <= h:
                    if ret[to_pop-1][1] <=h:
                        ret.pop(to_pop)
                    else:
                        #ret[to_pop][1] = h
                        to_fix.append(to_pop)
                        to_pop += 1
                else:
                    to_pop += 1
            # r 삽입할 위치  = to pop 이고 현재 to pop 은 r보다 오른쪽이다
            if ret[to_pop - 1][1] >=h:
               pass
            else:
                r_valid = True
                r_pos = to_pop
                if l_valid:
                    r_pos += 1
                r_h = ret[to_pop - 1][1]
                #ret.insert(to_pop, [r, ret[to_pop - 1][1]])
            if to_fix:
                for index in to_fix:
                    ret[index][1] = h
            if l_valid:
                ret.insert(l_pos, [l,h])
            if r_valid:
                ret.insert(r_pos, [r,r_h])


        return ret[:-1]



sol = Solution()
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]  # l r h
print(sol.getSkyline(buildings))