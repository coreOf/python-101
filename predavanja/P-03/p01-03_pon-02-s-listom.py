# +---+  Napisi program koji u ulaznom nizu 
# | 2 |  od n brojeva pronalazi najmanji i 
# +---+  ispisuje njegov redni broj

n = int(input("Duljina niza: "))

L = []
for rb in range(1, n+1):
    L.append(int(input()))

min_L = min(L)
min_rb = L.index(min_L) + 1

print("Najmanji na r.b.", min_rb)
