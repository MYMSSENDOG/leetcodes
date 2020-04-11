class Solution:
    def room(self, wanted_room, number_of_room) -> int:
        def merge(array, cur):
            if not array:
                array.append([i,i])
                return i

            l, r = 0, len(array)
            while l < r:
                m = (l + r) // 2
                start, end = array[m]
                if end < cur:
                    l = m+1
                elif start > cur:
                    r = m
                else:
                    array[m][1] +=1
                    ret = array[m][1]
                    if m < len(array) - 1:
                        if array[m][1] + 1 == array[m+1][0]:
                            array[m][1] = array[m+1][1]
                            array.pop(m+1)
                    return ret
            inserted = False
            if l >0:
                prev = array[l-1][1]
                if cur - 1 == prev:
                    array[l-1][1] = cur
                    inserted = True
            if l < len(array):
                next = array[l][0]
                if cur + 1 == next:
                    array[l][0] = cur
                    inserted = True

            if l < len(array) and l > 0:
                prev = array[l - 1][1]
                next = array[l][0]
                if prev == next:
                    array[l-1][1] = array[l][1]
                    array.pop(l)
            if not inserted:
                array.insert(l, [cur,cur])
            return cur
        array = []
        ret = []
        for i in wanted_room:
            ret.append(merge(array, i))
        return ret

sol = Solution()
wanted_room = [1,3,4,1,1,1,1]
number_of_room = 10**6
print(sol.room(wanted_room, number_of_room))