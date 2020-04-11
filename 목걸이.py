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

x = [sum(array[0 : N//3]),0,N//3]
y = [sum(array[N//3 : 2*N//3]),N//3, 2*N//3]
z = [sum(array[2*N//3 : ]),2*N//3, 0]
integrate = [x,y,z]

for i in range(N + 1):
    integrate.sort()
    big = integrate[2]
    small = integrate[0]
    minimal = min(big[0] - small[0], minimal)

    if minimal == possible_min:
        break

    if big[1] == small[2]:
        small[0] += array[small[2]]
        big[0] -= array[small[2]]

        small[2] = (small[2] + 1)%N
        big[1] = (big[1] + 1)%N

    elif big[2] == small[1]:
        small[1] = (small[1] - 1) % N
        big[2] = (big[2] - 1) % N

        small[0] += array[small[1]]
        big[0] -= array[small[1]]
print(minimal)






