from random import randint
a = [randint(1, 5) for i in range(30)]
n = 30
x = 0
y = 0
for i in range(0, n):
    if a[i] == 4 or a[i] == 5:
        x += a[i]
        y += 1
print(x/y) 

