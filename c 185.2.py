import collections
class Solution:
    def displayTable(self, orders):
        d = collections.defaultdict(dict)
        food = {}
        table = {}
        for order in orders:
            p, n, f = order
            food[f] = 1
            table[n] = 1
        foods = []
        tables = []
        for i in food:
            foods.append(i)
        for i in table:
            tables.append(i)
        foods.sort()
        tables.sort(key = lambda x: int(x))

        for order in orders:
            p, n, f = order
            if f in d[n]:
                d[n][f] +=1
            else:
                d[n][f] = 1



        ret = [["table"]]

        ret[0]+=(foods)
        for i in tables:
            temp = [str(i)]
            for dinner in foods:
                if dinner in d[i]:
                    temp.append(str(d[i][dinner]))
                else:
                    temp.append("0")
            ret.append(temp)
        return ret






sol = Solution()
orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(sol.displayTable(orders))