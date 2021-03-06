import sys

numbers = []
for line in sys.stdin:
    numbers.append([int(s) for s in line.split()])

L, _, _ = numbers[0]

connections = {}
for x, y, y2 in numbers[1:]:
    connections[(x, y)] = (x + 1, y2)
    connections[(x + 1, y2)] = (x, y)

x = 1
y = L
while y > 0:
    x, y = connections.get((x, y), (x, y))
    y -= 1
print(x)