N = int(input("Unesi broj elemenata liste: "))

L = []
for i in range(N):
    b = int(input("Unesi " + str(i+1) + ". element: "))
    L.append(b)

for x in L:
    if x % 2 == 0:
        print(x)
