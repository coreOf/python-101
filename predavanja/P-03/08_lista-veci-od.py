# unesi broj N i listu od N elemenata
# unesi broj G (granica)
# ispisi sve brojeve liste koji su veci od G

# 4
# 8 -4 3 5
# 0

N = int(input())
L = []
for i in range(N):
    L.append(int(input()))
G = int(input())

for b in L:
    if b > G:
        print(b)


