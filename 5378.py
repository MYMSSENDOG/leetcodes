class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ret = ""
        array = [[a,"a"], [b,"b"], [c,"c"]]
        array.sort(reverse= True)
        while 1:
            top = array[0][0]
            mid = array[1][0]
            bot = array[2][0]
            if top > mid+bot and top >1:
                ret += array[0][1] * 2
                array[0][0] -=2
            elif top:
                ret += array[0][1]
                array[0][0] -= 1
            top = array[0][0]
            if mid + bot == 0:
                break
            if mid:
                if mid + bot >top and mid >1:
                    ret += array[1][1] * 2
                    array[1][0] -=2
                elif mid >0:
                    ret += array[1][1] * 1
                    array[1][0] -= 1
            elif bot:
                if bot > top and bot>1:
                    ret += array[2][1] * 2
                    array[2][0] -= 2
                elif bot >0:
                    ret += array[2][1] * 1
                    array[2][0] -= 1

        return ret




sol = Solution()
a = 0
b = 1
c = 7
print(sol.longestDiverseString(a,b,c))