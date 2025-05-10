x = int(input())
x_copy = x
zbr = 0
while x > 0:
    z = x % 10
    x = x // 10
    zbr = zbr + z
print("Zbroj znamenki broja", x_copy, "je", zbr)