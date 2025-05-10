# zadana je lista L
# iz liste izbaci sva pojavljivanja broja 0
# prilikom izbacivanja zelimo ispisati s kojeg mjesta smo izbacili nulu

L = [3, 7, -2, 0, 4, 0, 1]
# L = [7, 5, 0, 1]
# L = [1, 2, 3, 4, -1]

b = L.count(0)

start = 0
for i in range(b):
    print(L)
    print("Izbacujem nulu na indeksu ", L.index(0, start))
    start = L.index(0, start) + 1


for i in range(b):
    L.remove(0)
    print()

print(L)