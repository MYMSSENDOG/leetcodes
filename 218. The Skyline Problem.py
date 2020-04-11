class Solution:
    def getSkyline(self, buildings):
        def deal_building(i):
            if i not in cur_building:
                cur_building.append(i)
            else:
                cur_building.pop(cur_building.index(i))

        if not buildings or not buildings[0]:
            return []
        new_buildings = []
        for i,e  in enumerate(buildings):
            l, r, h = e
            new_buildings.append([l, h, i])
            new_buildings.append([r, h, i])
        new_buildings.sort()



        ret = []
        cur_building = []
        i = 0
        while i < len(new_buildings):
            x= new_buildings[i][0]
            end = i
            while end < len(new_buildings) and new_buildings[end][0] == x:
                idx = new_buildings[end][2]
                deal_building(idx)
                end +=1

            critical_point = []
            if cur_building:
                max_height = max([buildings[id][1] for id in cur_building])
                if ret and ret[-1][1] == max_height:
                    pass
                else:
                    critical_point = [x, max_height]
            else:
                critical_point = [x,0]
            if critical_point:
                ret.append(critical_point)
            i = end
        return ret
sol = Solution()
buildings = [[0,2,3],[2,5,3]]  # l r h
print(sol.getSkyline(buildings))