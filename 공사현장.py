
x,y,R = input().split()
x = int(x)
y = int(y)
R = int(R)
n = input()
for i in range(int(n)):
    c_x, c_y = input().split()
    c_x = int(c_x)
    c_y = int(c_y)
    if (c_x - x)**2 + (c_y - y)**2 > R**2:
        print("silent")
    else:
        print("noisy")