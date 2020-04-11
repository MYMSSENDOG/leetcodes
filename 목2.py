input_line = input()
N = int(input_line)

S = input()

array = [0] * N
minimal = 1000000
possible_min = 1

if N%3 == 0:
    possible_min = 0


for i in range(N):
    array[i] = int(S[i])
sum = sum(array)
dp = [[]for i in range(N)]
d_sum = array[0]
i = 0
while d_sum + array[i+1]<=sum//3:
    d_sum += array[i+1]
    i+=1
dp[0] = [d_sum, i]
for k in range(1,N):
    d_sum -= array[k-1]
    while d_sum + array[(i + 1)%N] <= sum // 3:
        d_sum += array[(i + 1)%N]
        i = (i + 1)%N
    dp[k] = [d_sum, i]
for i in range(N):
    small = dp[i][0]
    middle = dp[(dp[i][1]+1)%N][0]
    big = sum- small - middle
    if minimal== possible_min:
        break
    boundary =dp[(dp[i][1]+1)%N][1]
    while middle<small:
        boundary = (boundary+1)%N
        middle += array[boundary]
        big -= array[boundary]
    minimal = min(minimal, max(middle, big) - small)
    while big >= small:
        boundary = (boundary+1)%N
        middle += array[boundary]
        big -= array[boundary]
        minimal = min(minimal, max(middle, big) - small)
    """
    middle = [dp[(dp[i][1]+1)%N][0], (dp[i][1] + 1)%N, dp[(dp[i][1]+1)%N][1]]

    big = [sum- small[0] - middle[0], (dp[(dp[i][1]+1)%N][0] + 1 )%N, (i-1)%N]
    while middle[0]<small[0]:
        
        middle[0] += array[(middle[2] + 1)%N]
        big[0] -= array[(middle[2] + 1)%N]
        middle[2] = (middle[2] + 1)%N
        big[1] = (middle[2] + 1)%N
    minimal = min(minimal, max(middle[0], big[0]) - small[0])
    while big[0] >= small[0]:
        middle[0] += array[(middle[2] + 1) % N]
        big[0] -= array[(middle[2] + 1) % N]
        middle[2] = (middle[2] + 1) % N
        big[1] = (middle[2] + 1) % N
        minimal = min(minimal, max(middle[0], big[0]) - small[0])
    """
print(minimal)







