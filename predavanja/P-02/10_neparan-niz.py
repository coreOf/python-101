# Unosimo N prirodnih brojeva
# Zelimo ispisati je li medu
# tih n brojeva bilo visekratnika broja 10

n = int(input())
v = "NE"
for i in range(n):
    b = int(input())
    if b % 10 == 0:
        v = "DA"

print(v)

# Npr. N=3
# Ulaz: 5, 20, 7
# Izlaz: DA

# Npr. N=4
# Ulaz: 5, 2, 7, 19
# Izlaz: NE

# Npr. N=6
# Ulaz: 5, 102, 70, 190, 15, 80
# Izlaz: DA
