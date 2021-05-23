import turtle as t

with open('turtle.txt', 'r') as f:
    lines = f.readlines()
    values = list(map(int, lines))

t.shape('turtle')
n = len(values)

for i in range(0, n - 1, 1):
    t.forward(values[i])
    t.left(values[i+1])