input_line = input().split()

k = int(input_line[0])
s = int(input_line[1])
t = int(input_line[2])

dp = [0] * k
dp[0] = "ABC"
for i in range(1,k):
    dp[i] = "A" + dp[i-1] + "B" + dp[i-1] + "C"
print(dp[-1][s-1:t])