# Unosimo N prirodnih brojeva
# Zelimo ispisati zadnji parni
# broj koji se pojavio, a ako nema
# parnih brojeva ispisujemo "Nema!"

n = int(input())
parni = 0
for i in range(n):
    b = int(input())
    if b % 2 == 0:
        parni = b

if parni == 0:
    print("Nema")
else:
    print(parni)

# Npr. N=5
# Ulaz: 3, 4, 2, 1, 7
# Izlaz: 2

# Npr. N=8
# Ulaz: 1, 4, 3, 1, 7, 9, 8, 10
# Izlaz: 10

# Npr. N=4
# Ulaz: 1, 21, 3, 7
# Izlaz: Nema
