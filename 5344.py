from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = date1.split("-")
        y2, m2, d2 = date2.split("-")
        start = date(int(y1), int(m1), int(d1))
        end = date(int(y2),int(m2),int(d2))
        dif = end-start
        return abs(dif.days)

sol = Solution()
date1 = "2019-06-29"
date2 = "2019-06-30"
print(sol.daysBetweenDates(date1, date2))

"""


a b c d e ...
2*sum - i

"""