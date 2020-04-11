class Solution:
    def readBinaryWatch(self, num: int):
        """
        4 , 6
        :param num:
        :return:
        """
        hour = [8, 4, 2, 1]
        minute = [32, 16, 8, 4, 2, 1]
        def combi(array, n, t):
            if t == "hour":
                if n == 0:
                    return ["0"]
                else:
                    ret = []
                    for i in range(len(array)-  n +1 ):
                        ret += [str(array[i] + int(k)) for k in combi(array[i+1:], n-1, t) if array[i] + int(k) <=11]
                    return ret
            else:
                if n == 0:
                    return ["0"]
                else:
                    ret = []
                    for i in range(len(array) - n + 1):
                        ret += [str(array[i] + int(k)) for k in combi(array[i + 1:], n - 1, t) if array[i] + int(k) <= 59]
                    return ret

        h = [0] * 5
        m = [0] * 7
        for i in range(5):
            h[i] = [ _ for _ in combi(hour, i, "hour")]
        for i in range(7):
            m[i] = [_ for _ in combi(minute, i, "m")]
            for j in range(len(m[i])):
                if len(m[i][j]) == 1:
                    m[i][j] = "0" + m[i][j]
        ret = []
        for i in range(max(0, num - 6), min(4, num)+1):
            for a in h[i]:
                for b in m[num-i]:
                    ret += [a + ":" + b]
        return ret
sol = Solution()
n = 2
print(sorted(sol.readBinaryWatch(n)))
