b = int(input())
s = 0
for i in range(4):
    z = b % 10
    s += z
    print(z)
    b //= 10
print(s)
