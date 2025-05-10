# +---+  Napisi program koji u ulaznom nizu 
# | 2 |  od n brojeva pronalazi najmanji i 
# +---+  ispisuje njegov redni broj

n = int(input("Duljina niza: "))

min_x = 0
min_rb = 1

for rb in range(1, n+1):
    x = int(input())
    if (rb == 1):
        min_x = x
    elif (x < min_x):
        min_x = x
        min_rb = rb

print("Najmanji na r.b.", min_rb)
