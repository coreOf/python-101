n = int(input("Unesi koliko brojeva zelis unijeti: "))

L = []

for i in range(n):
    b = int(input("Unesi broj: "))
    L.append(b)

print("Pomocu for x in L:")
# kad nam nije bitno na kojem smo elementu liste trenutno
for x in L:
    print(x)

print("Pomocu for i in range:")
# kad nam je bitno na kojem smo elementu trenutno
for i in range(len(L)):
    print(L[i])

# print(sum(L))
s = sum(L)
print("Zbroj unesenih brojeva je:", s)