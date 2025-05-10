# unesi broj N i listu od N elemenata
# unesi broj D (djelitelj)
# ispisi sve brojeve liste koji su djeljivi s brojem D

# 4
# 8 -4 3 5
# 2

N = int(input())
L = []
for i in range(N):
    L.append(int(input()))
D = int(input())

for b in L:
    if b % D == 0:
        print(b)


