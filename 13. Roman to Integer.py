input = ["III","IV","IX","LVIII","MCMXCIV"]
roman = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D": 500, "M":1000}

for s in input:
    ret = 0
    prev = 10000
    for c in s:
        cur = roman[c]
        if prev < cur:
            ret -= 2*prev
        ret += cur
        prev = cur
    print(ret)
