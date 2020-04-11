input_line = input().split()

n = int(input_line[0])#총갯수
k = int(input_line[1])#연속된 갯수
#총 경우의 수 2 **n
if k == 1:
    print(0)
if k == 2:
    print (1/2**(n-1))
else:
    dp = [0]*(n)
    dp[0] = 0
    dp[1] = 1
    ret = 2**n
    minus = 1
    for i in range(k-1):
        dp[i] = 2**i
    for i in range(k-1,n):

        for j in range(i-1,max(i-k,- 1),-1):
            dp[i] += dp[j]
    print((dp[-1] * 2)/ret)




