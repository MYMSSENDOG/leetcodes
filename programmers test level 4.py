def solution(begin, end):
    def get_prime_number(n):
        ret = []
        num = [True] * (int((n**(1/2)))+1)
        m = len(num)
        if m < 2:
            return ret
        i = 2
        while i <m:
            p = num[i]
            ret+=[i]
            for k in range(i,m,i):
                num[k] = False
            while i < m and num[i]==False:
                i+=1
        return ret
    primes = get_prime_number(end)
    answer = [1] * (end - begin + 1)
    for i in range(begin, end + 1):
        for p in primes:
            if i % p == 0:
                answer[i-begin] = i // p
                break
    if begin == 1:
        answer[0] = 0
    return answer
"""
    primes = get_prime_number(end)
    answer = [0] * (end - begin + 1)
    for i in range(begin, end+1):
        if answer[begin - i] !=0:
            continue
        for p in primes:
            if i % p == 0:
                for k in range(i, end+1, p):
                    if answer[k-begin] == 0:
                        answer[k-begin] = k//p
                break

    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = 1
    if begin == 0:
        answer[0] = 0
    return answer
"""


print(solution(1,10))