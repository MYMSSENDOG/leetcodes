class Solution:
    def getSkyline(self, buildings):
        ret = [[buildings[0][0],buildings[0][2]], [buildings[0][1],0],[9999999999999,0]]
        for i, coord in enumerate(buildings[1:],1):
            l,r,h = coord
            j = 0
            while ret[j][0]<=l:
                j += 1
                pass
            if ret[j-1][i] >=h :
                pass
            else:
                pass
                #ret.insert(j, [l,h])
            to_pop = j+1# r 은 여기부터 검사

            while ret[to_pop][0] <= r:
                if ret[to_pop][1] <=h:
                    ret.pop(to_pop)
                else:
                    to_pop += 1
            #r 삽입할 위치  = to pop 이고 현재 to pop 은 r보다 오른쪽이다
            if ret[to_pop-1][1]>=h:
                pass
                #do nothing
            else:
                ret.insert(to_pop, [r, ret[to_pop-1][1]])
        return ret
    """
    오른쪽 내려오는데 다른게 있으면 그점에 생김
    
    """





sol = Solution()
buildings = [ [2, 9, 10], [3, 7 ,15], [5, 12, 12], [15, 20 ,10], [19, 24 ,8] ]# l r h
print(sol.getSkyline(buildings))