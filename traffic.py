def solution(lines):
    answer = 0
    start = []
    end = []
    n = len(lines)
    for x in lines:
        log = x.split()
        time = log[-2].split(":")
        start_time = 0
        ex_time = float(log[-1].rstrip("s"))*1000
        mult = 1000
        for t in reversed(time):
            start_time += float(t) * mult
            mult *= 60
        start += [start_time- ex_time + 1]
        end += [start_time]

    ei = 0
    si = 0
    start.sort()
    p = 0

    while ei < n:
        et = end[ei]
        while si <n and start[si] - et < 1000:
            si += 1
            p+=1


        answer = max(answer, p)
        ei += 1
        p -=1
    return answer

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))