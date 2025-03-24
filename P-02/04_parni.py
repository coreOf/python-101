# Unosimo N prirodnih brojeva i
# ispisujemo koliko od njih je parno

n = int(input())
br = 0
for i in range(n):
    b = int(input())
    if b % 2 == 0:
        br += 1
print(br)
