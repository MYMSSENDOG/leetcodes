def solution(s):
    answer = 99999999
    m = len(s)
    for i in range(1, m//2+1):
        index = i
        cur = s[:i]
        ret = 0
        count = 1
        while index < m:
            if index + i >m:
                ret += i
                if count != 1:
                    ret += len(str(count))
                ret += (m - index)
                break

            next = s[index: index+i]
            if next == cur:
                count +=1
            else:
                cur = next
                if count != 1:
                    ret += len(str(count))
                count = 1
                ret += i
            index += i
        if m % i == 0:
            ret += i
            if count != 1:
                ret += len(str(count))
        answer = min(answer, ret)
    return answer




s = "a"
print(solution(s))