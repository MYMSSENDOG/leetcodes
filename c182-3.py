import collections
class UndergroundSystem:

    def __init__(self):
        self.d = collections.defaultdict(dict)
        self.start = collections.defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName, t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ss, st = self.start[id]
        d = self.d
        if stationName in d[ss]:
            d[ss][stationName][0] += 1
            d[ss][stationName][1]+=t - st
        else:
            d[ss][stationName] = [1, t-st]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        a, b = self.d[startStation][endStation]
        return b / a

code = ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
args = [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
U = UndergroundSystem()

for i, e in enumerate(code[1:],1):
    arg = args[i]
    if e == "checkIn":
        a, b, c = arg
        print(U.checkIn(a,b,c))
    if e == "checkOut":
        a, b, c = arg
        print(U.checkOut(a,b,c))
    if e == "getAverageTime":
        a,b = arg
        print(U.getAverageTime(a,b))
