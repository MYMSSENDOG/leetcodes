"""
input_line = input().split()

k = int(input_line[0])
s = int(input_line[1])
t = int(input_line[2])
"""
k = 10
s = 123
t = 139
dp_word = [""] * 10
dp_word[0] = "ABC"
dp = [0] * k
dp[0] = 3

for i in range(1,10):
    dp_word[i] = "A" + dp_word[i - 1] + "B" + dp_word[i - 1] + "C"

if k <=9:
    print(dp_word[k-1][s-1:t])
else:
    for i in range(1, k):
        dp[i] = 3 + 2 * dp[i-1]

    def position(k,i):
        if k <=10:
            return dp_word[k-1][i-1]
        c = dp[k-2]
        if i == 1:
            return "A"
        elif i == c+2:
            return "B"
        elif i == 2*c+3:
            return "C"
        elif i<c+2:
            return position(k-1,i-1)
        else:
            return position(k-1,i-2-c)
    st = ""
    for i in range(s, t+1):
        st += position(k,i)
    print(st)